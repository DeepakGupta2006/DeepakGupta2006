#!/usr/bin/env python3
"""Fetches your public GitHub stats (GraphQL) and writes data/stats.json.
Runs inside GitHub Actions with the built-in GITHUB_TOKEN. No setup needed."""
import json, os, sys, urllib.request, datetime as dt, pathlib

LOGIN = os.environ.get("GH_LOGIN") or os.environ.get("GITHUB_REPOSITORY_OWNER") or "DeepakGupta2006"
TOKEN = os.environ.get("GITHUB_TOKEN", "")
OUT = pathlib.Path(__file__).resolve().parent.parent / "data" / "stats.json"

QUERY = """
query($login:String!){
  user(login:$login){
    followers{totalCount}
    pullRequests{totalCount}
    issues{totalCount}
    repositories(ownerAffiliations:OWNER, isFork:false, first:100){
      totalCount
      nodes{ stargazerCount languages(first:10, orderBy:{field:SIZE, direction:DESC}){ edges{ size node{ name color } } } }
    }
    contributionsCollection{
      contributionCalendar{ totalContributions weeks{ contributionDays{ date contributionCount } } }
    }
  }
}"""

def gql():
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"login": LOGIN}}).encode(),
        headers={"Authorization": f"bearer {TOKEN}", "Content-Type": "application/json", "User-Agent": "profile-stats"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)

def streaks(days):
    """days: list of (date, count) sorted by date. Returns current, longest, longest_start, longest_end."""
    longest = cur = 0; l_start = l_end = None; run_start = None
    for d, n in days:
        if n > 0:
            if cur == 0: run_start = d
            cur += 1
            if cur > longest: longest, l_start, l_end = cur, run_start, d
        else:
            cur = 0
    today = dt.date.today().isoformat()
    seq = [n for d, n in days if d <= today]
    if seq and seq[-1] == 0: seq = seq[:-1]      # today isn't over yet
    current = 0
    for n in reversed(seq):
        if n > 0: current += 1
        else: break
    return current, longest, l_start, l_end

def main():
    data = gql()
    if "errors" in data or not data.get("data", {}).get("user"):
        print("GraphQL error:", data.get("errors") or data); sys.exit(1)
    u = data["data"]["user"]
    days = [(d["date"], d["contributionCount"])
            for w in u["contributionsCollection"]["contributionCalendar"]["weeks"] for d in w["contributionDays"]]
    days.sort()
    cur, lon, ls, le = streaks(days)
    langs = {}
    for repo in u["repositories"]["nodes"]:
        for e in repo["languages"]["edges"]:
            n = e["node"]["name"]; langs.setdefault(n, [0, e["node"]["color"] or "#8b949e"])[0] += e["size"]
    total = sum(v[0] for v in langs.values()) or 1
    top = sorted(langs.items(), key=lambda kv: -kv[1][0])
    out = {
        "login": LOGIN,
        "contributions": u["contributionsCollection"]["contributionCalendar"]["totalContributions"],
        "stars": sum(r["stargazerCount"] for r in u["repositories"]["nodes"]),
        "prs": u["pullRequests"]["totalCount"],
        "issues": u["issues"]["totalCount"],
        "repos": u["repositories"]["totalCount"],
        "followers": u["followers"]["totalCount"],
        "streak_current": cur, "streak_longest": lon, "streak_start": ls, "streak_end": le,
        "languages": [{"name": k, "pct": round(100 * v[0] / total, 1), "color": v[1]} for k, v in top[:8]],
        "updated": dt.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"),
    }
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print("wrote", OUT)

if __name__ == "__main__":
    main()
