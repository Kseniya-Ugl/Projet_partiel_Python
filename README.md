# Projet_partiel_Python
Partiel IA M1 DA LM Kseniya UGLITSKIKH


ksugl@LAPTOP-MHHG8J6R MINGW64 ~ (main)
$ cd C:/Users/ksugl/PycharmProjects/pythonProject

ksugl@LAPTOP-MHHG8J6R MINGW64 ~/PycharmProjects/pythonProject (main)
$ git init
Initialized empty Git repository in C:/Users/ksugl/PycharmProjects/pythonProject/.git/

ksugl@LAPTOP-MHHG8J6R MINGW64 ~/PycharmProjects/pythonProject (master)
$ git add.
git: 'add.' is not a git command. See 'git --help'.

The most similar command is
        add

ksugl@LAPTOP-MHHG8J6R MINGW64 ~/PycharmProjects/pythonProject (master)
$ git add
Nothing specified, nothing added.
hint: Maybe you wanted to say 'git add .'?
hint: Turn this message off by running
hint: "git config advice.addEmptyPathspec false"

ksugl@LAPTOP-MHHG8J6R MINGW64 ~/PycharmProjects/pythonProject (master)
$ git add .
warning: LF will be replaced by CRLF in .idea/inspectionProfiles/profiles_settings.xml.
The file will have its original line endings in your working directory

ksugl@LAPTOP-MHHG8J6R MINGW64 ~/PycharmProjects/pythonProject (master)
$ git add fibonacci.py

ksugl@LAPTOP-MHHG8J6R MINGW64 ~/PycharmProjects/pythonProject (master)
$ git add polynome.py

ksugl@LAPTOP-MHHG8J6R MINGW64 ~/PycharmProjects/pythonProject (master)
$ git add main.py

ksugl@LAPTOP-MHHG8J6R MINGW64 ~/PycharmProjects/pythonProject (master)
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   .idea/.gitignore
        new file:   .idea/inspectionProfiles/profiles_settings.xml
        new file:   .idea/misc.xml
        new file:   .idea/modules.xml
        new file:   .idea/pythonProject.iml
        new file:   fibonacci.py
        new file:   main.py
        new file:   polynome.py


ksugl@LAPTOP-MHHG8J6R MINGW64 ~/PycharmProjects/pythonProject (master)
$ git commit -m "initial commit"
[master (root-commit) ad1acea] initial commit
 8 files changed, 76 insertions(+)
 create mode 100644 .idea/.gitignore
 create mode 100644 .idea/inspectionProfiles/profiles_settings.xml
 create mode 100644 .idea/misc.xml
 create mode 100644 .idea/modules.xml
 create mode 100644 .idea/pythonProject.iml
 create mode 100644 fibonacci.py
 create mode 100644 main.py
 create mode 100644 polynome.py

ksugl@LAPTOP-MHHG8J6R MINGW64 ~/PycharmProjects/pythonProject (master)
$ git remote add origin https://github.com/Kseniya-Ugl/Projet_partiel_Python.git

ksugl@LAPTOP-MHHG8J6R MINGW64 ~/PycharmProjects/pythonProject (master)
$ git remote -v
origin  https://github.com/Kseniya-Ugl/Projet_partiel_Python.git (fetch)
origin  https://github.com/Kseniya-Ugl/Projet_partiel_Python.git (push)

ksugl@LAPTOP-MHHG8J6R MINGW64 ~/PycharmProjects/pythonProject (master)
$ git push -f origin master
remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
fatal: Authentication failed for 'https://github.com/Kseniya-Ugl/Projet_partiel_Python.git/'

ksugl@LAPTOP-MHHG8J6R MINGW64 ~/PycharmProjects/pythonProject (master)
$ ^C

ksugl@LAPTOP-MHHG8J6R MINGW64 ~/PycharmProjects/pythonProject (master)
$ git remote add origin git@github.com:Kseniya-Ugl/Projet_partiel_Python.git
error: remote origin already exists.

ksugl@LAPTOP-MHHG8J6R MINGW64 ~/PycharmProjects/pythonProject (master)
$ git push -f origin master
fatal: Le code d'état de réponse n'indique pas la réussite : 401 (Unauthorized).
error: unable to read askpass response from 'C:/Program Files/Git/mingw64/bin/git-askpass.exe'

ksugl@LAPTOP-MHHG8J6R MINGW64 ~/PycharmProjects/pythonProject (master)
$ git push -u origin main
error: src refspec main does not match any
error: failed to push some refs to 'https://github.com/Kseniya-Ugl/Projet_partiel_Python.git'

ksugl@LAPTOP-MHHG8J6R MINGW64 ~/PycharmProjects/pythonProject (master)
$ git remote add origin git@github.com:Kseniya-Ugl/Projet_partiel_Python.git
error: remote origin already exists.

ksugl@LAPTOP-MHHG8J6R MINGW64 ~/PycharmProjects/pythonProject (master)
$ git push -f origin master
Enumerating objects: 12, done.
Counting objects: 100% (12/12), done.
Delta compression using up to 8 threads
Compressing objects: 100% (10/10), done.
Writing objects: 100% (12/12), 1.82 KiB | 929.00 KiB/s, done.
Total 12 (delta 0), reused 0 (delta 0), pack-reused 0
remote:
remote: Create a pull request for 'master' on GitHub by visiting:
remote:      https://github.com/Kseniya-Ugl/Projet_partiel_Python/pull/new/master
remote:
To https://github.com/Kseniya-Ugl/Projet_partiel_Python.git
 * [new branch]      master -> master

ksugl@LAPTOP-MHHG8J6R MINGW64 ~/PycharmProjects/pythonProject (master)
$
