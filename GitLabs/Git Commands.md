## GIT Commands

**git remote -m** 
ukáže v jakém jsem repositáři (úložišti) </p>

**git status**
vypíše všechny soubory v aktuálním adresáři </p>

**git status -uno**
ukáže, jestli mám aktuální změny v projektu </p>

**git checkout** <nazev_vetve>
nebo </p>

**git switch** <nazev_vetve> </p>
přepnout na jinou větev <nazev_vetve> </p>

**git checkout .**
smaže všechny změny </p>

**git stash** </p>git

**git stash apply** 
dočasné úložiště změn (použití před git merge, když mám nějaké
necommitnuté změny) přiřazení změn do projektu git merge <nazev_vetve> sloučení změn do větve <nazev_vetve>
(vezme všechny commity, které jsou v remotu a plácne je do branche, kterou mám na localu)

**git rebase**
(Vezme všechny změny, které mám navíc oproti remotu a hodí si je někde mimo. Potom přidá všechny novinky z remotu na sebe a až pak přidá všechny moje commity. Dělá to postupně) </p>

**git branch**
vrátí soupis větví </p>

**git branch -d <nazev_vetve>**
(-d nahrazuje --delete) odstraní větev jen v případě, že už byla větev plně sloučena do své upstream větve 

**git branch -D <nazev_vetve>**
odstraní větev na localu bez ohledu na její souč. stav </p>

**git reflog**
vrátí nedávnou historii s gitem (Git sleduje aktualizace na špičce větví pomocí mechanismu nazývaného referenční protokoly nebo „reflogy“). V historii si podle hlavičky např. HEAD@{4} vyberu, kam se chci vrátit a do příkazu zadám při náležící hashtag (git checkout <hashtag>)

**git reset HEAD@{4} --hard**
vrátí mne na dané místo – POZOR!!! --hard zahodí všechny necommitnuté změny git checkout -b <nova_vetev> vytvoření nové větve <nova_vetev>git log vrátí seznam všech commitů – historii mého úložištěgit log -n3 vrátí seznam tří nejnovějších commitů do repositáře </p>

**git add <novy_soubor.txt>**
vytvoří mi v projektu nový soubor </p>

**git push <remote_name> --delete <branch_name>**
smaže vzdálenou větev (remote branch) </p>

**git fetch**
ukáže, co bylo nového commitnuto (přidáno) </p>

**git pull**
používá k načtení a stažení obsahu ze vzdáleného úložiště a okamžité aktualizaci místního úložiště spojené git fetch a git merge

**git add .** + **git commit -m**
„added něco – popis změn“ nebo

**git commit -a -m**
(nahradí předchozí dva příkazy ) </p>
