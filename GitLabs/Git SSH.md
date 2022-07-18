# SSH

```
ubuntu@UbuntuPC:~/PycharmProjects/Python-Training-Center$ cd ~/.ssh
ubuntu@UbuntuPC:~/.ssh$ ls
github  github.pub  id_ed25519  id_ed25519.pub  known_hosts
ubuntu@UbuntuPC:~/.ssh$ cat



ubuntu@UbuntuPC:~/.ssh$ cat id_ed25519.pub 
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIEt/dMYQhhVRuRNpj7LQq4UaDJywGaQ0P19mSTPoB/j2 jaromirbaca88@gmail.com
ubuntu@UbuntuPC:~/.ssh$ cd -
/home/ubuntu/PycharmProjects/Python-Training-Center
ubuntu@UbuntuPC:~/PycharmProjects/Python-Training-Center$ git pull
Username for 'https://github.com': ^C
ubuntu@UbuntuPC:~/PycharmProjects/Python-Training-Center$ git remote -v
origin  https://github.com/StingrayCZ/Python-Training-Center.git (fetch)
origin  https://github.com/StingrayCZ/Python-Training-Center.git (push)
ubuntu@UbuntuPC:~/PycharmProjects/Python-Training-Center$ git remote rm origin 
ubuntu@UbuntuPC:~/PycharmProjects/Python-Training-Center$ git remote -v
ubuntu@UbuntuPC:~/PycharmProjects/Python-Training-Center$ git remote add
usage: git remote add [<options>] <name> <url>

    -f, --fetch           fetch the remote branches
    --tags                import all tags and associated objects when fetching
                          or do not fetch any tag at all (--no-tags)
    -t, --track <branch>  branch(es) to track
    -m, --master <branch>
                          master branch
    --mirror[=(push|fetch)]
                          set up remote as a mirror to push to or fetch from

ubuntu@UbuntuPC:~/PycharmProjects/Python-Training-Center$ git remote add origin git@github.com:StingrayCZ/Python-Training-Center.git
ubuntu@UbuntuPC:~/PycharmProjects/Python-Training-Center$ git push
fatal: The current branch master has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin master

ubuntu@UbuntuPC:~/PycharmProjects/Python-Training-Center$ git init
Reinitialized existing Git repository in /home/ubuntu/PycharmProjects/Python-Training-Center/.git/
ubuntu@UbuntuPC:~/PycharmProjects/Python-Training-Center$ ls -a
 .                                     'SQL Labs.md'
 ..                                     Test.py
 CapturedAliendTech.md                 'Tips & Tricks.md'
'CSV Labs.md'                          '05 April 2022'
 Databaze.ipynb                        '1st 2nd SDA Lesson .md'
'DICT, TUPLE, SET, LIST labs.md'       '10th Lesson SDA (30.10.2021).md'
'DJango Labs'                          '11th Lesson SDA (31.10.2021).md'
'DJango labs (26Feb 2020).md'          '12th Lesson SDA (13.11.2021).md'
 Faker.py                              '13th Lesson SDA (14.11.2021).md'
 .git                                  '14th Lesson SDA (20.11.2021).md'
 GitLabs                               '15th Lesson SDA (21.11.2021).md'
'HTMl + CSS + JavaScript'              '16th Lesson SDA (27.11.2021).md'
'HTML Training'                        '17th lesson (28.11.2021).md'
 .idea                                 '18th lesson (11.12.2021).md'
 Ideas                                 '19th lesson (12.12.2021).md'
'IMPORT Methods.md'                    '20th lesson (18.12.2021).md'
 Jupyter.md                             2021_11_20_python_intermediate_session3.ipynb
 KEYWORDS.md                           '21th lesson (15.1.2022).md'
 KeyWords.PNG                          '22nd lesson (15-16.1.2022).md'
'Loop Labs (For).md'                   '23rd Lesson (22.1.2022).md'
'Loop Labs (While).md'                 '24th Lesson SDA (29.1.2022).md'
'OOP Object Oriented Programming'      '25th Lesson SDA (30.1.2022).md'
 Operator.PNG                          '26th Lesson (12Feb2022).md'
'PANDAS lib.ipynb'                     '26-27 March 2022 Django Lesson'
'PANDAS reseni.ipynb'                  '3rd SDA Lesson .md'
 Photos                                '4nd SDA Lesson (2-10-2021) .md'
'Python Begginer Course (YouTube).md'  '5nd Lesson SDA (3.10.2021).md'
'Python Book.md'                       '6nd Lesson SDA (16.10.2021).md'
'Python TEMP'                          '7nd Lesson SDA (17.10.2021).md'
 README.md                             '8nd Lesson SDA (23.10.2021).md'
'Recommended Training.md'              '9nd Lesson SDA (24.10.2021).md'
 Recursion.md
ubuntu@UbuntuPC:~/PycharmProjects/Python-Training-Center$ git status 
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   .idea/workspace.xml
        modified:   Ideas/dest.txt

no changes added to commit (use "git add" and/or "git commit -a")
ubuntu@UbuntuPC:~/PycharmProjects/Python-Training-Center$ git add Ideas/dest.txt 
ubuntu@UbuntuPC:~/PycharmProjects/Python-Training-Center$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   Ideas/dest.txt

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   .idea/workspace.xml

ubuntu@UbuntuPC:~/PycharmProjects/Python-Training-Center$ git commit -m "test commitu"
[master 148170c] test commitu
 1 file changed, 1 insertion(+), 4 deletions(-)
ubuntu@UbuntuPC:~/PycharmProjects/Python-Training-Center$ git push
fatal: The current branch master has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin master

ubuntu@UbuntuPC:~/PycharmProjects/Python-Training-Center$ git status 
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   .idea/workspace.xml

no changes added to commit (use "git add" and/or "git commit -a")
ubuntu@UbuntuPC:~/PycharmProjects/Python-Training-Center$ git push
fatal: The current branch master has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin master

ubuntu@UbuntuPC:~/PycharmProjects/Python-Training-Center$ git push --set-upstream origin master 
Warning: Permanently added the ECDSA host key for IP address '140.82.121.3' to the list of known hosts.
Enumerating objects: 29, done.
Counting objects: 100% (29/29), done.
Delta compression using up to 4 threads
Compressing objects: 100% (23/23), done.
Writing objects: 100% (26/26), 6.59 KiB | 281.00 KiB/s, done.
Total 26 (delta 7), reused 0 (delta 0)
remote: Resolving deltas: 100% (7/7), completed with 3 local objects.
To github.com:StingrayCZ/Python-Training-Center.git
   422b486..148170c  master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
ubuntu@UbuntuPC:~/PycharmProjects/Python-Training-Center$ ^C
ubuntu@UbuntuPC:~/PycharmProjects/Python-Training-Center$  cd -
/home/ubuntu/.ssh
ubuntu@UbuntuPC:~/.ssh$ 

```

git commit -m "Test commit 19.6.2022"

git add .

clear

git init

cd Python-Training-Center/

git init

git status

git add Ideas/dest.txt 

git commit -m "Test commitu"

git push *CHYBA*

**************************************

ls -al ~/.ssh

ssh-keygen -t ed25519 -C "jaromirbaca88@gmail.com"

```sqlite
Generating public/private ed25519 key pair.
Enter file in which to save the key (/home/ubuntu/.ssh/id_ed25519): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/ubuntu/.ssh/id_ed25519
Your public key has been saved in /home/ubuntu/.ssh/id_ed25519.pub
The key fingerprint is:
SHA256:TDcEe0bynjiafddqJ6Z7FlBt77IO+cJVifOS3yycPg0 jaromirbaca88@gmail.com
The key's randomart image is:
+--[ED25519 256]--+
|        o.o  .   |
|         *  . o  |
|        o *. ....|
|       o *.o o .o|
|        S o.  +o |
|       + .  .=E..|
|      o . ..+++B.|
|         . .O+B.+|
|          oB.*+o |
+----[SHA256]-----+
```


eval "$(ssh-agent -s)"

```sqlite
Agent pid 191887
```

ls -al ~/.ssh

```sqlite
celkem 28
drwx------  2 ubuntu ubuntu 4096 čen 19 10:45 .
drwxr-xr-x 30 ubuntu ubuntu 4096 čen 19 10:03 ..
-rw-------  1 ubuntu ubuntu 3389 kvě 21 09:51 github
-rw-r--r--  1 ubuntu ubuntu  749 kvě 21 09:51 github.pub
-rw-------  1 ubuntu ubuntu  419 čen 19 10:45 id_ed25519
-rw-r--r--  1 ubuntu ubuntu  105 čen 19 10:45 id_ed25519.pub
-rw-r--r--  1 ubuntu ubuntu  444 kvě 21 10:22 known_hosts
```

ssh-add ~/.ssh/id_ed25519

```
Identity added: /home/ubuntu/.ssh/id_ed25519 (jaromirbaca88@gmail.com)
```

cat ~/.ssh/id_ed25519.pub
```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIEt/dMYQhhVRuRNpj7LQq4UaDJywGaQ0P19mSTPoB/j2 jaromirbaca88@gmail.com
```


# Zasah mentora

ssh-keygen -t ed25519 -C "jaromirbaca88@gmail.com"

```
Generating public/private ed25519 key pair.
Enter file in which to save the key (/home/ubuntu/.ssh/id_ed25519): 
/home/ubuntu/.ssh/id_ed25519 already exists.
Overwrite (y/n)?
```

ls
```sqlite
 CapturedAliendTech.md                 'Tips & Tricks.md'
'CSV Labs.md'                          '05 April 2022'
 Databaze.ipynb                        '1st 2nd SDA Lesson .md'
'DICT, TUPLE, SET, LIST labs.md'       '10th Lesson SDA (30.10.2021).md'
'DJango Labs'                          '11th Lesson SDA (31.10.2021).md'
'DJango labs (26Feb 2020).md'          '12th Lesson SDA (13.11.2021).md'
 Faker.py                              '13th Lesson SDA (14.11.2021).md'
 GitLabs                               '14th Lesson SDA (20.11.2021).md'
'HTMl + CSS + JavaScript'              '15th Lesson SDA (21.11.2021).md'
'HTML Training'                        '16th Lesson SDA (27.11.2021).md'
 Ideas                                 '17th lesson (28.11.2021).md'
'IMPORT Methods.md'                    '18th lesson (11.12.2021).md'
 Jupyter.md                            '19th lesson (12.12.2021).md'
 KEYWORDS.md                           '20th lesson (18.12.2021).md'
 KeyWords.PNG                           2021_11_20_python_intermediate_session3.ipynb
'Loop Labs (For).md'                   '21th lesson (15.1.2022).md'
'Loop Labs (While).md'                 '22nd lesson (15-16.1.2022).md'
'OOP Object Oriented Programming'      '23rd Lesson (22.1.2022).md'
 Operator.PNG                          '24th Lesson SDA (29.1.2022).md'
'PANDAS lib.ipynb'                     '25th Lesson SDA (30.1.2022).md'
'PANDAS reseni.ipynb'                  '26th Lesson (12Feb2022).md'
 Photos                                '26-27 March 2022 Django Lesson'
'Python Begginer Course (YouTube).md'  '3rd SDA Lesson .md'
'Python Book.md'                       '4nd SDA Lesson (2-10-2021) .md'
'Python TEMP'                          '5nd Lesson SDA (3.10.2021).md'
 README.md                             '6nd Lesson SDA (16.10.2021).md'
'Recommended Training.md'              '7nd Lesson SDA (17.10.2021).md'
 Recursion.md                          '8nd Lesson SDA (23.10.2021).md'
'SQL Labs.md'                          '9nd Lesson SDA (24.10.2021).md'
 Test.py
```

cd ~/.ssh
ls
```sqlite
github  github.pub  id_ed25519  id_ed25519.pub  known_hosts
```
cat id_ed25519.pub 
```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIEt/dMYQhhVRuRNpj7LQq4UaDJywGaQ0P19mSTPoB/j2 jaromirbaca88@gmail.com
```
cd -
```
/home/ubuntu/PycharmProjects/Python-Training-Center
```
git pull
```sqlite
ubuntu@UbuntuPC:~/PycharmProjects/Python-Training-Center$ git pull
Username for 'https://github.com': ^C  #ukonceni relace
```

git remote -v

```sqlite
origin  https://github.com/StingrayCZ/Python-Training-Center.git (fetch)
origin  https://github.com/StingrayCZ/Python-Training-Center.git (push)
```

git remote rm origin 

git remote -v

git remote add

```sqlite
usage: git remote add [<options>] <name> <url>

    -f, --fetch           fetch the remote branches
    --tags                import all tags and associated objects when fetching
                          or do not fetch any tag at all (--no-tags)
    -t, --track <branch>  branch(es) to track
    -m, --master <branch>
                          master branch
    --mirror[=(push|fetch)]
                          set up remote as a mirror to push to or fetch from
```

git remote add origin git@github.com:StingrayCZ/Python-Training-Center.git

git push
```sqlite
fatal: The current branch master has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin master
```

git init
```sqlite
 .                                     'SQL Labs.md'
 ..                                     Test.py
 CapturedAliendTech.md                 'Tips & Tricks.md'
'CSV Labs.md'                          '05 April 2022'
 Databaze.ipynb                        '1st 2nd SDA Lesson .md'
'DICT, TUPLE, SET, LIST labs.md'       '10th Lesson SDA (30.10.2021).md'
'DJango Labs'                          '11th Lesson SDA (31.10.2021).md'
'DJango labs (26Feb 2020).md'          '12th Lesson SDA (13.11.2021).md'
 Faker.py                              '13th Lesson SDA (14.11.2021).md'
 .git                                  '14th Lesson SDA (20.11.2021).md'
 GitLabs                               '15th Lesson SDA (21.11.2021).md'
'HTMl + CSS + JavaScript'              '16th Lesson SDA (27.11.2021).md'
'HTML Training'                        '17th lesson (28.11.2021).md'
 .idea                                 '18th lesson (11.12.2021).md'
 Ideas                                 '19th lesson (12.12.2021).md'
'IMPORT Methods.md'                    '20th lesson (18.12.2021).md'
 Jupyter.md                             2021_11_20_python_intermediate_session3.ipynb
 KEYWORDS.md                           '21th lesson (15.1.2022).md'
 KeyWords.PNG                          '22nd lesson (15-16.1.2022).md'
'Loop Labs (For).md'                   '23rd Lesson (22.1.2022).md'
'Loop Labs (While).md'                 '24th Lesson SDA (29.1.2022).md'
'OOP Object Oriented Programming'      '25th Lesson SDA (30.1.2022).md'
 Operator.PNG                          '26th Lesson (12Feb2022).md'
'PANDAS lib.ipynb'                     '26-27 March 2022 Django Lesson'
'PANDAS reseni.ipynb'                  '3rd SDA Lesson .md'
 Photos                                '4nd SDA Lesson (2-10-2021) .md'
'Python Begginer Course (YouTube).md'  '5nd Lesson SDA (3.10.2021).md'
'Python Book.md'                       '6nd Lesson SDA (16.10.2021).md'
'Python TEMP'                          '7nd Lesson SDA (17.10.2021).md'
 README.md                             '8nd Lesson SDA (23.10.2021).md'
'Recommended Training.md'              '9nd Lesson SDA (24.10.2021).md'
 Recursion.md
```

git status

```
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   .idea/workspace.xml
        modified:   Ideas/dest.txt

no changes added to commit (use "git add" and/or "git commit -a")
```