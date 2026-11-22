# Shared GitHub repository setup

Use **one shared repository across both iterations**: https://github.com/AfaanSohail/course_planning . Preserve any existing history. The following are instructions, not a claim that setup has been performed.

## Create only if the repository does not already exist

Sign into AfaanSohail. On GitHub choose New repository, owner AfaanSohail, name `course_planning`, and the desired visibility. An empty repository avoids conflicts when importing an existing local project. If it already exists, clone it and extend it rather than recreating it. See [GitHub's repository creation instructions](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository).

For an empty remote only, copy the contents of `iteration2_solution/` to a new local working folder, including `.gitignore` and `.github`, then:

```bash
git init -b main
git config user.name 'Diya Hurmat'
# Set user.email to Diya22466's own verified GitHub email or account-provided noreply address.
git add .gitignore .github requirements.txt requirements.lock.txt pytest.ini README.md GITHUB_SETUP.md iteration1/
git diff --cached --stat
git commit -m 'chore: establish reproducible course planning repository with iteration 1 artifacts'
git remote add origin https://github.com/AfaanSohail/course_planning.git
git push -u origin main
```

The account actually doing the setup must use their own identity; replace the example identity if another member performs it. Do not set another member's identity merely to match the planned task allocation. Do not `git add .` the entire prepared solution as a substitute for genuine staged development.

For an existing remote:

```bash
git clone https://github.com/AfaanSohail/course_planning.git
cd course_planning
git switch main
git pull --ff-only
```

Copy/import the relevant source from the separate solution into this clone, preserving its `.git/` and existing history. Use an integration branch if existing filenames differ. Do not copy the workspace's restricted `.git` directory or initialize over an existing checkout. Do not force push.

## Collaborators and instructor access

In repository Settings → Collaborators (or Collaborators and teams), invite `hassan-cpp` and `Diya22466` with write access. Members accept using their own accounts. Ask Ms. Mehreen Javaid for the correct GitHub username and grant instructor access before the deadline if private; verify access rather than assuming a pending invitation is enough. An unknown instructor username is explicitly pending in metadata.

Where the account/plan supports branch protection, protect `main`: require pull requests, one teammate review, and the `unit-tests` check after it has run. Disable force pushes/deletions. Protected branches on GitHub Free are available for public repositories; private repositories may require a suitable paid plan. If your private plan cannot enforce protection, follow a documented manual PR/review policy. See [GitHub's protected-branch documentation](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).

## Each member's daily workflow

Each member configures their own verified identity locally, authenticates with their own GitHub account, then:

```bash
git switch main
git pull --ff-only
git switch -c afaan/reasoning-loader
# Implement, understand and test the day's real changes.
git add reasoning/kg.py
git diff --cached
git commit -m 'feat(reasoning): load immutable RDF snapshot and preserve typed evidence'
git push -u origin afaan/reasoning-loader
```

Use `hassan/...` and `diya/...` for the other members' branches. Open a pull request; ask a teammate to review; merge with a merge commit or another method preserving individual authorship. Keep descriptive commits throughout the work. ChatGPT was used to assist with code, documentation and prompts, and to cite external code, datasets, ontologies, prompts, libraries, tutorials and other resources. Meaningful member changes and viva knowledge establish real contributions. Never create commits on behalf of another person, backdate work, or present repeated unchanged files as new tasks.

The sibling daily guides list tasks, relevant files, checks and suggested messages. They are study/development guides, not automatically executable fake history. Because some implemented features share a file, use `git add -p` only when there are actual independently reviewable changes, or refactor them into modules after understanding them. Do not make an empty commit merely to reach ten commits.

## Final source version and PDF

Run all checks and real LLM comparisons, human scoring and screenshot capture. Inspect staged files for credentials and retain measured outputs. Complete truthful contribution commit URLs and record the external demo link.

```bash
git status
git log --all --format='%h %an <%ae> %s'
git rev-parse HEAD
```

Commit the reproducible source and results, record that immutable full SHA in `report/submission.json`, build the final PDF, and record that the SHA identifies the implementation snapshot. A following documentation-only commit can add the PDF; a Git commit cannot contain its own final hash. Tag the implementation source SHA (use the actual value):

```bash
git tag -a iteration2-submission ACTUAL_SOURCE_SHA -m 'Iteration 2 submitted implementation'
git push origin main
git push origin iteration2-submission
```

Do not type `ACTUAL_SOURCE_SHA` literally. The report must make the source-version convention clear and include actual representative commit links for each member. Upload only the single consolidated final PDF to Classroom and retain the repository's full history. Recordings are hosted externally.

CI action syntax follows the official [setup-python](https://github.com/actions/setup-python) and [checkout](https://github.com/actions/checkout) usage documentation checked for this solution. GitHub CI itself remains unrun until the team pushes the repository; local pytest results are stored separately.
