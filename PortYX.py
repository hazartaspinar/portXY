import os # İlk Önce "OS" Kütüphanesi'ni Projemize Ekliyoruz.
import webbrowser

os.system("apt-get install figlet") # Sanal Bir Terminal Açıp Figlet Aracını İndiriyoruz.
os.system("apt-get install lolcat") # Sanal Bir Terminal Açıp Lolcat Aracını İndiriyoruz.
os.system("clear")# Sanal Terminal'i Temizliyoruz.
os.system("figlet -f Electronic PortYX | lolcat -a -d 1")# Şekilli Yazı Yazıyoruz.

Ad = input("Lütfen Adınızı Giriniz --> ")# Kullanıcıdan Adını Yazmasını İstiyoruz.

os.system("clear")# Sanal Terminal'i Temizliyoruz.



print("""

                           ########                 #
                      #################            #
                   ######################         #
                  #########################      #
                ############################
               ##############################
               ###############################
              ###############################
              ##############################
                              #    ########   #
                 ##        ###        ####   ##
                                      ###   ###
                                    ####   ###
               ####          ##########   ####
               #######################   ####
                 ####################   ####
                  ##################  ####
                    ############      ##
                       ########        ###
                      #########        #####
                    ############      ######
                   ########      #########
                     #####       ########
                       ###       #########
                      ######    ############
                     #######################
                     #   #   ###  #   #   ##
                     ########################
                      ##     ##   ##     ##
                                                                
-----------------------------------
1) \033[36mCtf İçin Tarama\033[0m 
-----------------------------------
2) \033[32mCtf İçin Tarama (Tüm Portlar)\033[0m
-----------------------------------
3) \033[31mServis Ve Versiyon Bilgisi\033[0m
-----------------------------------
4) \033[36mSitede Dizin Bulma\033[0m
-----------------------------------
5) \033[31mWhoİs Sorgusu\033[0m
-----------------------------------
6) \033[31mÖnerilen Kaynaklar\033[0m
-----------------------------------
7) \033[36mHava Durumu\033[0m
-----------------------------------
8) \033[36mKendini Test ET !!\033[0m
-----------------------------------
9) \033[36mKendini Test ET !! (İNDİR)\033[0m
-----------------------------------
2022) \033[35mPortyX'i Yapanlar :D \033[0m
""")# Şekilli Menü Yazdırıyoruz.

islemno = input("\033[31mLütfen İşlem Numaranızı Giriniz {} : --> \033[0m".format(Ad))# Kullanıcıdan Hangi İşlemi Yapmak İstiyorsa Onu Yazmasını İstiyoruz.


if(islemno == "1"):

    hedef1 = input("\033[31mLütfen Hedef İp'yi Giriniz {} : --> \033[0m".format(Ad))# Kullanıcıdan Hedef İP Bilgisini Girmesini İstiyoruz.

    os.system("sudo nmap -sS -sV -sC -Pn -O " + hedef1)

    baska1 = input("\033[31mBaşka Bir İşlem Yapmak İstermisiniz e/h {} : --> \033[0m".format(Ad))

    if(baska1 == "e"):
        os.system("python3 PortYX.py")
    else:
        os.system("figlet -f Electronic BYE | lolcat -a -d 1")

elif(islemno == "2"):

    hedef2 = input("\033[31mLütfen Hedef İp'yi Giriniz {} : --> \033[0m".format(Ad))

    os.system("sudo nmap -sS -sV -sC -Pn -p- -T5 " + hedef2)

    baska2 = input("\033[31mBaşka Bir İşlem Yapmak İstermisiniz e/h {} : --> \033[0m".format(Ad))

    if(baska2 == "e"):
        os.system("python3 PortYX.py")
    else:
        os.system("figlet -f Electronic BYE | lolcat -a -d 1")

elif(islemno == "3"):

    hedef3 = input("\033[31mLütfen Hedef İp'yi Giriniz {} : --> \033[0m".format(Ad))

    os.system("sudo nmap -sS -sV " + hedef3)

    baska3 = input("\033[31mBaşka Bir İşlem Yapmak İstermisiniz e/h {} : --> \033[0m".format(Ad))

    if(baska3 == "e"):
        os.system("python3 PortYX.py")
    else:
        os.system("figlet -f Electronic BYE | lolcat -a -d 1")

elif(islemno == "4"):

    print("""
    ******************************************************
    4.1) Dizin Bulma (Uzun Sürer !!)
    ******************************************************
    4.2) Dizin Bulma (Kısa Sürer !!)
    ******************************************************
    4.3) Dizin Bulma (HTTPS Sıkıntılı Sitelerde Kullanın)
    ******************************************************

    """)

    islemno1 = input("\033[35mLütfen İşlem Numaranızı Giriniz {} : --> \033[0m".format(Ad))

    if(islemno1 == "4.1"):

        hedef = input("\033[35mLütfen Hedef Siteyi Giriniz {} : --> \033[0m".format(Ad))

        os.system("sudo gobuster dir -u {} -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt".format(hedef))

        baska4 = input("\033[31mBaşka Bir İşlem Yapmak İstermisiniz e/h {} : --> \033[0m".format(Ad))

        if(baska4 == "e"):

            os.system("python3 PortYX.py")

        else:
            os.system("figlet -f Electronic BYE | lolcat -a -d 1")

    elif(islemno1 == "4.2"):

        hedef = input("\033[35mLütfen Hedef Siteyi Giriniz {} : --> \033[0m".format(Ad))

        os.system("sudo gobuster dir -u {} -w /usr/share/wordlists/dirb/common.txt".format(hedef))

        baska5 = input("\033[31mBaşka Bir İşlem Yapmak İstermisiniz e/h {} : --> \033[0m".format(Ad))

        if(baska5 == "e"):

            os.system("python3 PortYX.py")

        else:
            os.system("figlet -f Electronic BYE | lolcat -a -d 1")

    elif(islemno1 == "4.3"):

        hedef = input("\033[35mLütfen Hedef Siteyi Giriniz {} : --> \033[0m".format(Ad))

        os.system("sudo gobuster dir -u {} -w /usr/share/wordlists/dirb/common.txt -k".format(hedef))

        baska6 = input("\033[31mBaşka Bir İşlem Yapmak İstermisiniz e/h {} : --> \033[0m".format(Ad))

        if(baska6 == "e"):

            os.system("python3 PortYX.py")

        else:
            os.system("figlet -f Electronic BYE | lolcat -a -d 1")

    else:
        os.system("figlet -f Electronic HATA | lolcat -a -d 1")


elif(islemno == "5"):

    hedef = input("\033[35mLütfen Hedef Siteyi Giriniz {} : --> \033[0m".format(Ad))

    os.system("whois {}".format(hedef))

    baska7 = input("\033[31mBaşka Bir İşlem Yapmak İstermisiniz e/h {} : --> \033[0m".format(Ad))

    if(baska7 == "e"):

        os.system("python3 PortYX.py")

    else:
        os.system("figlet -f Electronic BYE | lolcat -a -d 1")


elif(islemno == "6"):

    print("""
    6.1) Nmap İle İlgili Video (NetworkChuck)
    *******************************************
    6.2) Nmap İle İlgili Video (Siber Kampüs)
    *******************************************
    6.3) Nmap İle İlgili Kaynak (Nmap.org)
    *******************************************
    6.4) Nmap İle İlgili Kaynak (TryHackme.com)
    *******************************************
    6.5) Takip Edilecek Kanal (NetworkChuck)
    *******************************************
    6.6) Takip Edilecek Kanal (David Bombal)
    *******************************************
    6.7) Takip Edilecek Kanak (SixPon)
    *******************************************
    6.8) Takip Edilecek Kanal (Mehmet D. INCE)
    *******************************************
    6.9) CTF Çalışalıcak Site (TryHackme.com)
    *******************************************
    7.0) CTF Çalışalıcak Site (HackTheBox.eu)
    *******************************************
    """)

    islemno2 = input("\033[35mLütfen İşlem Numaranızı Giriniz {} : --> \033[0m".format(Ad))


    if(islemno2 == "6.1"):
        webbrowser.open('https://www.youtube.com/watch?v=4t4kBkMsDbQ')

        baska8 = input("\033[31mBaşka Bir İşlem Yapmak İstermisiniz e/h {} : --> \033[0m".format(Ad))

        if(baska8 == "e"):

            os.system("python3 PortYX.py")

        else:
            os.system("figlet -f Electronic BYE | lolcat -a -d 1")


    elif(islemno2 == "6.2"):
        webbrowser.open('https://www.youtube.com/watch?v=8wC0746F6SQ&list=PLGWmuqrfJZRsDj0V8R2Nl-m4GQe9IIjjW')

        baska9 = input("\033[31mBaşka Bir İşlem Yapmak İstermisiniz e/h {} : --> \033[0m".format(Ad))

        if(baska9 == "e"):

            os.system("python3 PortYX.py")

        else:
            os.system("figlet -f Electronic BYE | lolcat -a -d 1")


    elif(islemno2 == "6.3"):
        webbrowser.open('https://nmap.org/book/man.html')

        baska10 = input("\033[31mBaşka Bir İşlem Yapmak İstermisiniz e/h {} : --> \033[0m".format(Ad))

        if(baska10 == "e"):

            os.system("python3 PortYX.py")

        else:
            os.system("figlet -f Electronic BYE | lolcat -a -d 1")


    elif(islemno2 == "6.4"):
        webbrowser.open('https://tryhackme.com/module/nmap')

        baska11 = input("\033[31mBaşka Bir İşlem Yapmak İstermisiniz e/h {} : --> \033[0m".format(Ad))

        if(baska11 == "e"):

            os.system("python3 PortYX.py")

        else:
            os.system("figlet -f Electronic BYE | lolcat -a -d 1")


    elif(islemno2 == "6.5"):
        webbrowser.open('https://www.youtube.com/@NetworkChuck')

        baska12 = input("\033[31mBaşka Bir İşlem Yapmak İstermisiniz e/h {} : --> \033[0m".format(Ad))

        if(baska12 == "e"):

            os.system("python3 PortYX.py")

        else:
            os.system("figlet -f Electronic BYE | lolcat -a -d 1")


    elif(islemno2 == "6.6"):
        webbrowser.open('https://www.youtube.com/@davidbombal')

        baska13 = input("\033[31mBaşka Bir İşlem Yapmak İstermisiniz e/h {} : --> \033[0m".format(Ad))

        if(baska13 == "e"):

            os.system("python3 PortYX.py")

        else:
            os.system("figlet -f Electronic BYE | lolcat -a -d 1")


    elif(islemno2 == "6.7"):
        webbrowser.open('https://www.youtube.com/@Sixpon')

        baska14 = input("\033[31mBaşka Bir İşlem Yapmak İstermisiniz e/h {} : --> \033[0m".format(Ad))

        if(baska14 == "e"):

            os.system("python3 PortYX.py")

        else:
            os.system("figlet -f Electronic BYE | lolcat -a -d 1")


    elif(islemno2 == "6.8"):
        webbrowser.open('https://www.youtube.com/@mdisec')

        baska15 = input("\033[31mBaşka Bir İşlem Yapmak İstermisiniz e/h {} : --> \033[0m".format(Ad))

        if(baska15 == "e"):

            os.system("python3 PortYX.py")

        else:
            os.system("figlet -f Electronic BYE | lolcat -a -d 1")


    elif(islemno2 == "6.9"):
        webbrowser.open('https://tryhackme.com/hacktivities')

        baska16 = input("\033[31mBaşka Bir İşlem Yapmak İstermisiniz e/h {} : --> \033[0m".format(Ad))

        if(baska16 == "e"):

            os.system("python3 PortYX.py")

        else:
            os.system("figlet -f Electronic BYE | lolcat -a -d 1")


    elif(islemno2 == "7.0"):
        webbrowser.open('https://www.hackthebox.com')

        baska17 = input("\033[31mBaşka Bir İşlem Yapmak İstermisiniz e/h {} : --> \033[0m".format(Ad))

        if(baska17 == "e"):

            os.system("python3 PortYX.py")

        else:
            os.system("figlet -f Electronic BYE | lolcat -a -d 1")

    else:
        os.system("figlet -f Electronic HATA | lolcat -a -d 1")


elif(islemno == "7"):

    os.system("curl wttr.in/~İstanbul")

    baska18 = input("\033[31mBaşka Bir İşlem Yapmak İstermisiniz e/h {} : --> \033[0m".format(Ad))

    if(baska18 == "e"):

        os.system("python3 PortYX.py")

    else:
        os.system("figlet -f Electronic BYE | lolcat -a -d 1")


elif(islemno == "8"):

    os.system("chmod +x linpeas.sh")
    os.system("sudo ./linpeas.sh")

    baska19 = input("\033[31mBaşka Bir İşlem Yapmak İstermisiniz e/h {} : --> \033[0m".format(Ad))

    if(baska19 == "e"):

        os.system("python3 PortYX.py")

    else:
        os.system("figlet -f Electronic BYE | lolcat -a -d 1")


elif(islemno == "9"):

    webbrowser.open('https://github.com/carlospolop/PEASS-ng/releases/tag/20221127')


    baska20 = input("\033[31mBaşka Bir İşlem Yapmak İstermisiniz e/h {} : --> \033[0m".format(Ad))

    if(baska20 == "e"):

        os.system("python3 PortYX.py")

    else:
        os.system("figlet -f Electronic BYE | lolcat -a -d 1")


elif(islemno == "2022"):
    os.system("figlet 1.Developer")
    os.system("figlet -f Electronic Burak | lolcat -a -d 5")



    os.system("figlet 2.Developer")
    os.system("figlet -f Electronic Atahan | lolcat -a -d 5")



    os.system("figlet 3.Developer")
    os.system("figlet -f Electronic Hazar | lolcat -a -d 5")



    os.system("figlet 4.Developer")
    os.system("figlet -f Electronic Yunus | lolcat -a -d 5")



    os.system("figlet 5.Developer")
    os.system("figlet -f Electronic Batu | lolcat -a -d 5")

















