import threading
import websocket


class Lock:
    def __init__(self):
        self.lock = threading.Lock()

    def __enter__(self):
        self.lock.acquire()

    def __exit__(self, *args):
        self.lock.release()


DEFAULTS = {
    "botname": "MELON",
    "botavatar": "https://cdn.discordapp.com/icons/133049272517001216/a_aab012f3206eb514cac0432182e9e9ec.gif?size=1024",
    "botinfo": "Melon is a bot designed to keep your server safe and engage your members. It has auto-mod capabilities that filter outs certain types of behavior when your staff team is not available. Melon has it's own custom giveaways system, donation logging system, leveling system, custom commands system, engaging-fun-commands, informative-commands, utility commands and more!",
    "owner": "inthedark.org#0666",
    "color": "yellow",
}

WS_URL = "ws://localhost:"
WS_EXCEPTIONS = (
    ConnectionRefusedError,
    websocket._exceptions.WebSocketConnectionClosedException,
    ConnectionResetError,
    ConnectionAbortedError,
)

ALLOWED_LOCALES = [
    "en",
    "af_ZA",
    "ar_SA",
    "bg_BG",
    "ca_ES",
    "cs_CZ",
    "da_DK",
    "de_DE",
    "el_GR",
    "es_ES",
    "fi_FI",
    "fr_FR",
    "he_IL",
    "hu_HU",
    "id_ID",
    "it_IT",
    "ja_JP",
    "ko_KR",
    "nl_NL",
    "pl_PL",
    "pt_BR",
    "pt_PT",
    "ro_RO",
    "ru_RU",
    "sk_SK",
    "sv_SE",
    "tr_TR",
    "uk_UA",
    "vi_VN",
    "zh_CN",
    "zh_HK",
    "zh_TW",
]
