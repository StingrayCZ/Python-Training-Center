# Generating a new SSH key and adding it to the ssh-agent

## Generating a new SSH key

```terminal
ssh-keygen -t ed25519 -C "jaromirbaca88@engineer.com"
```

# Generating a new SSH key for a hardware security key

```terminal
$ ssh-keygen -t ed25519-sk -C "your_email@example.com"
```

## Adding your SSH key to the ssh-agent
Before adding a new SSH key to the ssh-agent to manage your keys, you should have checked for existing SSH keys and generated a new SSH key.

## Adding your SSH key to the ssh-agent

• Start the ssh-agent in the background.

```terminal
$ eval "$(ssh-agent -s)"
> Agent pid 59566
```

• Add your SSH private key to the ssh-agent.

```terminal
$ ssh-add ~/.ssh/id_ed25519
```

## Adding a new SSH key to your GitHub account

```terminal
$ cat ~/.ssh/id_ed25519.pub
```

<p float="left">
  <img src="/Photos/GitHubKey.png" width="200" /> 
</p>

## Connection between Github&Pycharm
```terminal
git remote rm origin
git remote -v
git remote add
git remote add origin git@github:... .git
git push --set-upstream origin master
```