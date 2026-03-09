"""
RYTHME BOT — Telegram
Assistant personnel de Maxence
================================
Pour démarrer : python bot.py
"""

import telebot
import schedule
import threading
import time
import random
from datetime import datetime

# ─────────────────────────────────────────────────────────────
# CONFIGURATION — mets ton token ici
# ─────────────────────────────────────────────────────────────
BOT_TOKEN = "8750519237:AAGlIL3ENarVlHEsoe7VAh-rkOiqq3E18Rc"

bot = telebot.TeleBot(BOT_TOKEN, parse_mode='Markdown')

# Chat ID de Maxence (sauvegardé après /start)
chat_id = None
waiting_for = None  # suivi de quel check-in est en attente


# ─────────────────────────────────────────────────────────────
# CITATIONS MOTIVANTES
# ─────────────────────────────────────────────────────────────
QUOTES = [
    "\"Si tu veux comprendre l'univers, pense en termes d'énergie, de fréquence et de vibration.\" — Nikola Tesla",
    "\"La discipline est la liberté.\" — Jocko Willink",
    "\"Nous souffrons plus dans l'imagination que dans la réalité.\" — Sénèque",
    "\"Le succès n'est pas final, l'échec n'est pas fatal. C'est le courage de continuer qui compte.\" — Churchill",
    "\"Fais ce qui est difficile et le difficile deviendra facile.\" — Frank Herbert",
    "\"Le corps réalise ce que l'esprit croit.\" — Napoleon Hill",
    "\"Chaque matin tu as deux choix : continuer à dormir avec tes rêves, ou te lever et les réaliser.\"",
    "\"La vague ne te demande pas si tu es prêt. Elle arrive.\"",
    "\"Trois heures de travail vrai valent dix heures de présence.\" — Cal Newport",
    "\"Le rythme n'est pas une contrainte. C'est la forme que prend la liberté.\"",
    "\"Ce que tu fais chaque jour compte plus que ce que tu fais de temps en temps.\" — Gretchen Rubin",
    "\"L'énergie que tu mets dans ton matin détermine la qualité de ta journée entière.\"",
    "\"Sois l'observateur de tes pensées, pas leur esclave.\" — Bouddhisme",
    "\"Un arbre solide résiste à la tempête parce que ses racines sont profondes.\"",
    "\"Maîtrise toi toi-même avant de vouloir maîtriser quoi que ce soit d'autre.\" — Épictète",
    "\"Tu n'as pas à être parfait. Tu as juste à avancer.\"",
    "\"Le moment présent est le seul endroit où tu peux agir.\" — Eckhart Tolle",
    "\"Chaque vague que tu rates, c'est la prochaine qui compte.\"",
    "\"La vraie richesse c'est le temps maîtrisé, pas l'argent accumulé.\"",
    "\"Ton corps est ta première entreprise. Investis dedans d'abord.\"",
]

# ─────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────
def send(msg):
    """Envoie un message à Maxence."""
    if chat_id:
        try:
            bot.send_message(chat_id, msg, parse_mode='Markdown')
        except Exception as e:
            print(f"Erreur envoi message: {e}")

def save_chat_id(cid):
    with open('chat_id.txt', 'w') as f:
        f.write(str(cid))

def load_chat_id():
    try:
        with open('chat_id.txt', 'r') as f:
            return int(f.read().strip())
    except:
        return None


# ─────────────────────────────────────────────────────────────
# REMINDERS JOURNALIERS
# ─────────────────────────────────────────────────────────────
def remind_reveil():
    send(
        "☀️ *6h45 — RÉVEIL*\n\n"
        "Pas d'écran. Ouvre la fenêtre.\n"
        "Respire l'air du matin.\n\n"
        "_Tu es le créateur de ton univers._"
    )

def remind_lumiere():
    send(
        "🌅 *7h00 — EXPOSITION LUMIÈRE*\n\n"
        "5 min dehors ou fenêtre grande ouverte.\n"
        "Laisse la lumière recalibrer ton horloge interne."
    )

def remind_intention():
    send(
        "✍️ *7h10 — INTENTION DU JOUR*\n\n"
        "Papier + stylo. Écris :\n"
        "• Ton intention du jour\n"
        "• Tes 2 tâches non-négociables\n\n"
        "_Zéro écran pour l'instant._"
    )

def remind_yoga():
    send(
        "🧘 *7h20 — YOGA (40 min)*\n\n"
        "Salutation au soleil • Mobilité • Pranayama\n"
        "Shavasana 5 min à la fin.\n\n"
        "_Le corps s'éveille avant le mental._"
    )

def checkin_yoga():
    global waiting_for
    waiting_for = "yoga"
    send("🧘 *Check-in* — Tu as fait ton yoga ce matin ? _(oui / non)_")

def remind_dejeuner_matin():
    send(
        "☕ *8h00 — PETIT DÉJEUNER*\n\n"
        "Calme. Sans écran. Mange lentement.\n"
        "_Ce moment t'appartient._"
    )

def remind_quote_matin():
    send(f"💬 *Citation du jour*\n\n_{random.choice(QUOTES)}_")

def remind_bloc1():
    send(
        "⚡ *8h45 — BLOC 1 — DEEP WORK*\n\n"
        "📵 Téléphone en mode avion\n"
        "🎯 1 seule tâche\n"
        "🖥️ Plein écran\n\n"
        "_90 minutes d'intensité réelle. C'est parti._"
    )

def checkin_bloc1():
    global waiting_for
    waiting_for = "bloc1"
    send(
        "⚡ *Check-in Bloc 1*\n\n"
        "Terminé ? Qu'est-ce que tu as produit ?\n"
        "_(Réponds librement — j'écoute)_"
    )

def remind_pause():
    send(
        "🌿 *10h15 — PAUSE VRAIE (20 min)*\n\n"
        "Marche ou étirements.\n"
        "Zéro réseau. Zéro email.\n\n"
        "_Ton cerveau se recharge dans le silence._"
    )

def remind_bloc2():
    send(
        "⚡ *10h35 — BLOC 2 — DEEP WORK*\n\n"
        "📵 Téléphone en mode avion\n"
        "🎯 1 seule tâche\n"
        "🔥 Dernier bloc — donne tout\n\n"
        "_3h de focus = plus que 12h dispersées._"
    )

def remind_ecran_off():
    send(
        "🔴 *12h05 — ÉCRAN ÉTEINT*\n\n"
        "C'est terminé. Sans exception.\n"
        "Ferme tout. Pose l'ordi.\n\n"
        "_Tu as produit. Maintenant tu vis._"
    )

def remind_dejeuner():
    send(
        "🍽️ *12h15 — DÉJEUNER*\n\n"
        "Repas complet. Sans écran.\n"
        "Mange lentement. Goûte."
    )

def remind_sport():
    send(
        "🌊 *13h00 — SURF ou MUSCU*\n\n"
        "Corps présent, mental libre.\n"
        "_La mer ne reprogramme pas._\n\n"
        "Si surf disponible → surf gagne toujours."
    )

def checkin_sport():
    global waiting_for
    waiting_for = "sport"
    send(
        "🌊 *Check-in Sport*\n\n"
        "Session faite ? C'était quoi ?\n"
        "_(surf / muscu / autre — dis-moi)_"
    )

def remind_sunset():
    send(
        "🌇 *17h00 — MARCHE COUCHER DU SOLEIL*\n\n"
        "30-45 min. Dehors.\n"
        "Pas de scroll. Observe.\n\n"
        "_La lumière orangée ferme le cycle du jour._"
    )

def remind_winddown():
    send(
        "🌙 *20h30 — WIND DOWN*\n\n"
        "Lumière douce.\n"
        "Pas d'écran bleu.\n"
        "Lecture, musique calme, étirements doux.\n\n"
        "_La soirée appartient à ton corps._"
    )

def remind_reflexion():
    global waiting_for
    waiting_for = "reflexion"
    send(
        "📖 *21h30 — RÉFLEXION (10 min)*\n\n"
        "3 questions pour fermer la journée :\n\n"
        "1️⃣ Qu'est-ce que j'ai accompli aujourd'hui ?\n"
        "2️⃣ Qu'est-ce que j'ai bien géré ?\n"
        "3️⃣ Mon intention pour demain ?\n\n"
        "_Réponds quand tu veux. Je suis là._"
    )

def remind_sommeil():
    send(
        "💤 *22h30 — EXTINCTION*\n\n"
        "Chambre sombre et fraîche.\n"
        "Téléphone hors de la chambre — c'est sacré.\n\n"
        "_Bonne nuit Maxence. Tu as bien géré aujourd'hui._"
    )

def recap_dimanche():
    send(
        "📊 *BILAN DE SEMAINE — DIMANCHE*\n\n"
        "Prenons 5 min pour regarder en arrière.\n\n"
        "1️⃣ Combien de sessions yoga cette semaine ?\n"
        "2️⃣ Combien de séances surf / muscu ?\n"
        "3️⃣ Tu as respecté l'écran mort à 13h ?\n"
        "4️⃣ Sur 10 — comment tu évalues ta semaine ?\n"
        "5️⃣ Une chose à améliorer la semaine prochaine ?\n\n"
        "_Chaque réponse t'appartient. Je suis juste là pour écouter._"
    )


# ─────────────────────────────────────────────────────────────
# RÉPONSES AUX MESSAGES
# ─────────────────────────────────────────────────────────────
MOTS_OUI  = ["oui", "yes", "fait", "done", "yep", "ouais", "✅", "yess", "yas", "ok", "checked", "fais"]
MOTS_NON  = ["non", "no", "pas fait", "nope", "nan", "pas encore", "raté"]

ENCOURAGEMENTS = [
    "🔥 *Bien joué !* Chaque fois que tu honores ton protocole, tu te construis.",
    "💪 C'est ça. Le rythme se renforce un jour à la fois.",
    "⚡ Exactement ça. Tu es dans ton rythme, Maxence.",
    "🌊 Parfait. Continue comme ça — tu avances.",
    "✅ Noté. C'est une brique de plus dans la construction.",
]

RELANCES = [
    "Pas de jugement. La journée n'est pas finie.\n\nQu'est-ce qui t'en a empêché ?",
    "C'est ok. Une chose à la fois.\nTu peux encore le faire maintenant ?",
    "Le rythme se construit aussi dans les jours difficiles.\nDe quoi tu as besoin là ?",
    "Pas grave. Ce qui compte c'est demain matin.\nQu'est-ce qui a bloqué ?",
]


@bot.message_handler(commands=['start'])
def cmd_start(message):
    global chat_id
    chat_id = message.chat.id
    save_chat_id(chat_id)
    bot.send_message(
        chat_id,
        "🌅 *RYTHME BOT — Actif*\n\n"
        "Salut Maxence. Je suis ton assistant de rythme personnel.\n\n"
        "Je t'envoie des reminders, je te pose des questions et je te garde dans ton protocole — "
        "yoga, deep work, surf, dopamine, tout.\n\n"
        "*Commandes :*\n"
        "/planning — Voir le programme du jour\n"
        "/quote — Une citation pour te booster\n"
        "/recap — Bilan de semaine\n"
        "/regles — Tes règles d'or\n"
        "/aide — Cette aide\n\n"
        "_\"Le rythme n'est pas une contrainte. C'est la forme que prend la liberté.\"_"
    )


@bot.message_handler(commands=['planning', 'aide_planning'])
def cmd_planning(message):
    bot.send_message(
        message.chat.id,
        "📅 *TON PLANNING DU JOUR*\n\n"
        "6h45  ☀️  Réveil — pas d'écran\n"
        "7h00  🌅  Exposition lumière\n"
        "7h10  ✍️  Intention + 2 tâches\n"
        "7h20  🧘  Yoga (40 min)\n"
        "8h00  ☕  Petit déjeuner sans écran\n"
        "8h45  ⚡  *BLOC 1 — Deep Work (90 min)*\n"
        "10h15  🌿  Pause vraie (20 min)\n"
        "10h35  ⚡  *BLOC 2 — Deep Work (90 min)*\n"
        "12h05  🔴  *ÉCRAN ÉTEINT — sans exception*\n"
        "12h15  🍽️  Déjeuner\n"
        "13h00  🌊  Surf ou Muscu\n"
        "17h00  🌇  Marche coucher du soleil\n"
        "20h30  🌙  Wind down\n"
        "21h30  📖  Réflexion\n"
        "22h30  💤  Sommeil\n\n"
        "_3h de deep work = plus que 12h dispersées._"
    )


@bot.message_handler(commands=['quote'])
def cmd_quote(message):
    bot.send_message(message.chat.id, f"💬 _{random.choice(QUOTES)}_")


@bot.message_handler(commands=['recap'])
def cmd_recap(message):
    recap_dimanche()


@bot.message_handler(commands=['regles'])
def cmd_regles(message):
    bot.send_message(
        message.chat.id,
        "📋 *TES RÈGLES D'OR*\n\n"
        "1. 🧘  Yoga avant l'écran — toujours\n"
        "2. 📵  Pas d'email avant 9h\n"
        "3. 🔴  Écran mort à 13h — pas de négo\n"
        "4. 🚫  Pas d'écran en chambre\n"
        "5. 🌊  Surf prioritaire sur muscu\n"
        "6. 🧠  Pas de porno — jamais\n"
        "7. 🌿  1 jour en nature par mois\n"
        "8. ✨  Tu es le créateur de ton univers"
    )


@bot.message_handler(commands=['aide'])
def cmd_aide(message):
    bot.send_message(
        message.chat.id,
        "ℹ️ *AIDE — RYTHME BOT*\n\n"
        "/planning — Programme du jour heure par heure\n"
        "/quote — Citation motivante\n"
        "/recap — Bilan de semaine (5 questions)\n"
        "/regles — Tes règles d'or\n\n"
        "Tu peux aussi m'écrire librement :\n"
        "• _\"oui / fait / done\"_ → je valide ton check-in\n"
        "• _\"non / pas encore\"_ → on trouve une solution\n"
        "• _\"comment tu vas\"_ → je réponds\n"
        "• N'importe quel message → je suis là"
    )


@bot.message_handler(func=lambda m: True)
def handle_message(message):
    global waiting_for
    text = message.text.lower().strip() if message.text else ""

    is_oui = any(m in text for m in MOTS_OUI)
    is_non = any(m in text for m in MOTS_NON)

    # Réponse à un check-in en attente
    if waiting_for and (is_oui or is_non):
        if is_oui:
            bot.send_message(message.chat.id, random.choice(ENCOURAGEMENTS))
        else:
            bot.send_message(message.chat.id, f"💬 {random.choice(RELANCES)}")
        waiting_for = None

    # Réflexion du soir — texte libre
    elif waiting_for == "reflexion":
        bot.send_message(
            message.chat.id,
            "📝 Noté. C'est bien de prendre ce temps.\n\n"
            "_Bonne nuit Maxence. Demain est un nouveau rythme._"
        )
        waiting_for = None

    # Mots-clés généraux
    elif any(m in text for m in ["quote", "citation", "motive", "boost"]):
        bot.send_message(message.chat.id, f"💬 _{random.choice(QUOTES)}_")

    elif any(m in text for m in ["planning", "programme", "aujourd'hui", "schedule"]):
        cmd_planning(message)

    elif any(m in text for m in ["aide", "help", "commande"]):
        cmd_aide(message)

    elif any(m in text for m in ["recap", "bilan", "semaine"]):
        recap_dimanche()

    elif any(m in text for m in ["regle", "règle", "protocole"]):
        cmd_regles(message)

    # Réponse générique humaine
    else:
        reponses = [
            f"Je suis là. 🌅 Continue ton rythme.\n\n_{random.choice(QUOTES)}_",
            "Tu avances, Maxence. Un jour à la fois. 🌊",
            f"💬 _{random.choice(QUOTES)}_",
            "Le rythme se construit dans les petits gestes quotidiens. 🧘",
        ]
        bot.send_message(message.chat.id, random.choice(reponses))


# ─────────────────────────────────────────────────────────────
# PLANIFICATION DES REMINDERS
# ─────────────────────────────────────────────────────────────
def setup_schedule():
    # Matin
    schedule.every().day.at("06:45").do(remind_reveil)
    schedule.every().day.at("07:00").do(remind_lumiere)
    schedule.every().day.at("07:10").do(remind_intention)
    schedule.every().day.at("07:20").do(remind_yoga)
    schedule.every().day.at("07:58").do(checkin_yoga)       # check-in yoga
    schedule.every().day.at("08:00").do(remind_dejeuner_matin)
    schedule.every().day.at("08:30").do(remind_quote_matin)
    schedule.every().day.at("08:45").do(remind_bloc1)
    schedule.every().day.at("10:10").do(checkin_bloc1)      # check-in bloc 1
    schedule.every().day.at("10:15").do(remind_pause)
    schedule.every().day.at("10:35").do(remind_bloc2)

    # Milieu de journée
    schedule.every().day.at("12:05").do(remind_ecran_off)
    schedule.every().day.at("12:15").do(remind_dejeuner)
    schedule.every().day.at("13:00").do(remind_sport)
    schedule.every().day.at("14:35").do(checkin_sport)      # check-in sport

    # Après-midi / soir
    schedule.every().day.at("17:00").do(remind_sunset)
    schedule.every().day.at("20:30").do(remind_winddown)
    schedule.every().day.at("21:30").do(remind_reflexion)
    schedule.every().day.at("22:30").do(remind_sommeil)

    # Bilan hebdo le dimanche soir
    schedule.every().sunday.at("20:00").do(recap_dimanche)

    print("✅ Tous les reminders sont planifiés.")


def run_schedule():
    setup_schedule()
    while True:
        schedule.run_pending()
        time.sleep(30)


# ─────────────────────────────────────────────────────────────
# DÉMARRAGE
# ─────────────────────────────────────────────────────────────
if __name__ == '__main__':
    # Restaurer le chat_id si déjà connu
    saved = load_chat_id()
    if saved:
        chat_id = saved
        print(f"✅ Chat ID restauré : {chat_id}")
        send("🌅 *RYTHME Bot redémarré* — Je suis de retour Maxence.")
    else:
        print("📱 En attente de /start depuis Telegram...")

    # Lancer le scheduler en arrière-plan
    t = threading.Thread(target=run_schedule, daemon=True)
    t.start()

    print("🌅 RYTHME Bot actif. Ctrl+C pour arrêter.\n")

    # Polling Telegram
    bot.infinity_polling(timeout=30, long_polling_timeout=30)
