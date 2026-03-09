# RYTHME BOT — Guide d'installation (5 min)

## Étape 1 — Créer ton bot sur Telegram

1. Ouvre Telegram, cherche **@BotFather**
2. Envoie `/newbot`
3. Donne un nom : `Rythme Maxence`
4. Donne un username : `rythme_maxence_bot` (ou ce que tu veux)
5. BotFather te donne un **token** qui ressemble à ça :
   ```
   7412398765:AAGhbXk9mNpQrStUvWxYz1234567890abcd
   ```
6. **Copie ce token** — tu en as besoin à l'étape 3.

---

## Étape 2 — Installer Python (si pas déjà fait)

Vérifie si Python est installé :
```
python3 --version
```

Si tu vois `Python 3.x.x` → parfait, passe à l'étape 3.

Si pas installé → va sur [python.org/downloads](https://python.org/downloads) et installe Python 3.

---

## Étape 3 — Configurer le bot

Ouvre le fichier `bot.py` avec un éditeur de texte (TextEdit, VS Code, Notepad...).

Trouve cette ligne tout en haut :
```python
BOT_TOKEN = "METS_TON_TOKEN_ICI"
```

Remplace `METS_TON_TOKEN_ICI` par ton token de l'étape 1 :
```python
BOT_TOKEN = "7412398765:AAGhbXk9mNpQrStUvWxYz1234567890abcd"
```

Sauvegarde le fichier.

---

## Étape 4 — Installer les dépendances

Ouvre un terminal dans le dossier `rythme-bot` et lance :
```
pip3 install -r requirements.txt
```

---

## Étape 5 — Lancer le bot

```
python3 bot.py
```

Tu verras :
```
📱 En attente de /start depuis Telegram...
✅ Tous les reminders sont planifiés.
🌅 RYTHME Bot actif.
```

---

## Étape 6 — Connecte-toi au bot

1. Sur Telegram, cherche le username de ton bot (celui que tu as choisi)
2. Envoie `/start`
3. Le bot répond — c'est bon, tu es connecté !

**Le bot connaît maintenant ton numéro et t'enverra tous les reminders.**

---

## Commandes disponibles

| Commande | Action |
|----------|--------|
| `/start` | Démarrer / se reconnecter |
| `/planning` | Voir le programme du jour |
| `/quote` | Citation motivante |
| `/regles` | Tes règles d'or |
| `/recap` | Bilan de semaine |
| `/aide` | Cette aide |

Tu peux aussi lui écrire librement — il répond.

---

## Pour que le bot tourne en permanence

Le bot doit tourner sur ton ordinateur. Deux options :

**Option A — Ton Mac/PC allumé**
Lance le bot et laisse le terminal ouvert. Ça suffit.

**Option B — Hébergement gratuit (recommandé)**
Déploie sur [Railway.app](https://railway.app) ou [Render.com](https://render.com) — gratuit, cloud, tourne 24h/24 même si ton ordi est éteint. Me dire si tu veux qu'on fasse ça ensemble.

---

## Réponses que le bot comprend

- `oui / fait / done` → Il valide ton check-in
- `non / pas encore` → Il te relance doucement
- `quote / citation` → Il t'envoie une citation
- N'importe quel message → Il répond

---

*"Le rythme n'est pas une contrainte. C'est la forme que prend la liberté."*
