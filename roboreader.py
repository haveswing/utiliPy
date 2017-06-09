from gtts import gTTS
import os

print("\n-roboreader-\n\n")

def rr():
    u_imput = input("\n\ninserisci il testo da far pronunciare a roboreader: ")
    print("\nlettura testo in corso...\n")
    tts = gTTS(text=u_imput, lang='it')
    tts.save("roboreader_out.mp3")
    os.system("roboreader_out.mp3")
    print("\nla lettura del tuo testo è stata salvata.\n\nfile: roboreader_out.mp3\n")
    print("chiudi il programma o sovrascrivi l'output precedente con una nuova lettura.\n")

x = True

while x:
    rr()
