# CCF LAB 2

## 16.01.2017

## Ali Abdulmadzhidov

06:12	-	Found image of disk full of evidences.

07:12	-	Firstly made some standart procedures. 

```
> file primary-disk.dd 
primary-disk.dd: x86 boot sector, code offset 0x52, OEM-ID "NTFS    ", sectors/cluster 8, reserved sectors 0, Media descriptor 0xf8, heads 255, hidden sectors 2048, dos < 4.0 BootSector (0x80)
> sha512sum /data/Evidence/primary-disk.dd 
61d5573e1ac9e5aaf6da768e6967aa8fcf30907346877d6711ed2894f7d77d76586dc710da3f2516381d87e7cc4f91b85af74453f985d5663954b6f861c92cef  /data/Evidence/primary-disk.dd
> sha512sum /data/Evidence/primary-disk.dd 
61d5573e1ac9e5aaf6da768e6967aa8fcf30907346877d6711ed2894f7d77d76586dc710da3f2516381d87e7cc4f91b85af74453f985d5663954b6f861c92cef  /data/Evidence/primary-disk.dd
> md5sum /data/Evidence/primary-disk.dd 
2089ac80f6de29a64d53245c28239d385  /data/Evidence/primary-disk.dd
```

07:30	-	Mounted image in readonly

```
> mount -o ro /data/Evidence/primary-disk.dd /media
```

07:45	-	Started search for typical files *pdf, *jpg ...

```
> find /media -iname *.pdf -exec file {} \;
/media/$Recycle.Bin/S-1-5-21-1973456639-838052630-220784754-1000/$IW9UT7J.pdf: data
/media/$Recycle.Bin/S-1-5-21-1973456639-838052630-220784754-1000/$RW9UT7J.pdf: PDF document, version 1.3
/media/Program Files/TrueCrypt/TrueCrypt User Guide.pdf: PDF document, version 1.5
/media/Program Files/Adobe/Reader 8.0/Reader/IDTemplates/ENU/AdobeID.pdf: PDF document, version 1.6
/media/Program Files/Adobe/Reader 8.0/Reader/IDTemplates/ENU/DefaultID.pdf: PDF document, version 1.6
/media/Program Files/Adobe/Reader 8.0/Reader/PDFSigQFormalRep.pdf: PDF document, version 1.6
/media/Program Files/Adobe/Reader 8.0/Reader/plug_ins/Annotations/Stamps/ENU/Dynamic.pdf: PDF document, version 1.6
/media/Program Files/Adobe/Reader 8.0/Reader/plug_ins/Annotations/Stamps/ENU/SignHere.pdf: PDF document, version 1.4
/media/Program Files/Adobe/Reader 8.0/Reader/plug_ins/Annotations/Stamps/ENU/StandardBusiness.pdf: PDF document, version 1.4
/media/Program Files/Adobe/Reader 8.0/Reader/plug_ins/Annotations/Stamps/Words.pdf: PDF document, version 1.3
/media/Program Files/Adobe/Reader 8.0/Resource/ENUtxt.pdf: PDF document, version 1.3
/media/Users/jb/Documents/$RW9UT7J.pdf: PDF document, version 1.3
/media/Users/jb/Documents/explorer_of_the_seas.pdf: PDF document, version 1.3
/media/Users/jb/Documents/pass_uk_kane.pdf: PDF document, version 1.3
```



Found few interesting files. Passport of some M. Kane. And Interpol wanted screenshot.

 ![kaynepassp](/home/mrzizik/screenshots/kaynepassp.png)

 ![interpol](/home/mrzizik/screenshots/interpol.png)

 ![ocean](/home/mrzizik/screenshots/ocean.png)

Knowing that our user's name is "jb", we can suppose that he is Jason Born from USA, but he also has fake passwords. Also we have second subject - Marie Kreutz, from Germany.

In that folder we also have some keystore, but we don't know master password for now.

09:10	-	Scanned image for viruses. It is full of trojans and adware.

```
> clamscan -l /data/Evidence/clamscan.log -r -i /media

/media/Program Files/Adobe/Adobe Help Viewer/1.0/ahv.exe: Win.Trojan.Ramnit-7850 FOUND
/media/Program Files/Adobe/Reader 8.0/Reader/Acrofx32.dll: Win.Trojan.Ramnit-5459 FOUND
/media/Program Files/Adobe/Reader 8.0/Reader/adobe_eula.dll: Win.Trojan.Ramnit-5466 FOUND
/media/Program Files/Adobe/Reader 8.0/Reader/icucnv34.dll: Win.Trojan.Ramnit-7189 FOUND
/media/Program Files/BabylonToolbar/BabylonToolbar/1.5.3.17/BabylonToolbarApp.dll: Win.Adware.BHO-7316 FOUND
/media/Program Files/BabylonToolbar/BabylonToolbar/1.5.3.17/BabylonToolbarEng.dll: Win.Adware.BHO-7317 FOUND
/media/Program Files/BabylonToolbar/BabylonToolbar/1.5.3.17/BabylonToolbarsrv.exe: Win.Adware.BHO-7318 FOUND
/media/Program Files/BabylonToolbar/BabylonToolbar/1.5.3.17/BabylonToolbarTlbr.dll: Win.Adware.BHO-7319 FOUND
/media/Program Files/BabylonToolbar/BabylonToolbar/1.5.3.17/bh/BabylonToolbar.dll: Win.Adware.BHO-7320 FOUND
/media/Program Files/Common Files/Adobe/Updater5/AdobeUpdater.exe: Win.Trojan.Agent-1373820 FOUND
/media/Program Files/Java/jre6/bin/jpiexp.dll: Win.Trojan.Ramnit-7017 FOUND
/media/Users/jb/AppData/Local/Microsoft/Windows/Temporary Internet Files/Content.IE5/6VI08I0R/toolbar[1].exe: Win.Trojan.Agent-973588 FOUND
/media/Users/jb/AppData/Local/Mozilla/Firefox/Profiles/oq7c6xx8.default/Cache/A3E3FCA7d01: Win.Trojan.Downloader-60957 FOUND
/media/Users/jb/AppData/Local/Temp/2CD5E65E-BAB0-7891-8557-08019CE30634/MyBabylonTB.exe: Win.Adware.BHO-7320 FOUND
/media/Users/jb/AppData/Local/Temp/BabylonToolbar/BabylonToolbar/1.5.3.17/BabylonToolbar4ie.exe: Win.Adware.BHO-7320 FOUND
/media/Users/jb/AppData/LocalLow/Sun/Java/jre1.6.0_18/Data1.cab: Win.Trojan.Ramnit-7017 FOUND
/media/Users/mk/Desktop/UPS_INVOICE_TRNR_PLEASE_PRINT.DOC.exe: Win.Trojan.Generic-42 FOUND

----------- SCAN SUMMARY -----------
Known viruses: 4748140
Engine version: 0.97.5
Scanned directories: 2208
Scanned files: 14822
Infected files: 17
Total errors: 9
Data scanned: 2097.48 MB
Data read: 2894.78 MB (ratio 0.72:1)
Time: 497.601 sec (8 m 17 s)

```

10:10	-	Surfed trough directories to find something interesting. In /media/Users/jb/AppData/Local/Temp found password for keystore and opened it. Also there're some truecrypt container.

 ![passwd](/home/mrzizik/screenshots/passwd.png) 

 ![passwd1](/home/mrzizik/screenshots/passwd1.png)

10:15	-	Password for truecrypt container is in ower password store. Excellent. 

 ![passwd2](/home/mrzizik/screenshots/passwd2.png)

10:20	-	In container we have snapshots from some video.

![screen](/home/mrzizik/screenshots/screen.png)

10:25	-	Second password references us to commincation with some Pam. Try to find some mail data.

10:30	-	In  /media/Users/jb/AppData/Roaming/Thunderbird/Profiles/1w94q78u.default/Mail/gmx.ch/ we have local cache for sent and received mail.

 ![mail](/home/mrzizik/screenshots/mail.png)

 ![mail1](/home/mrzizik/screenshots/mail1.png)

 ![mail_answer](/home/mrzizik/screenshots/mail_answer.png)

 ![mail_answer2](/home/mrzizik/screenshots/mail_answer2.png)

They want to go to Naples? Also there're are 2 attachments in base64, that can be easily decoded.

This one we've already seen. 

 ![jaswanted](/home/mrzizik/screenshots/jaswanted.png)



 ![jaswanted](/home/mrzizik/screenshots/jaswanted.png)

 But here is something new. treadstone.zip archive. It is crypted. But we remember, that we have password for communicatoin with Pam. 

 ![passwdPAM](/home/mrzizik/screenshots/passwdPAM.png)

It absolutelly fits here. In pdf we have some more data about JB. His real name is Wasiliy Popov and he is from Saint Petersburg. Also he is CIA agent.

![treadstone](/home/mrzizik/screenshots/treadstone.png)

 ![treadstone1](/home/mrzizik/screenshots/treadstone1.png)

11:01	-	Digging deeper into cache files leads me to skype caches. Got some usernames and message parts.

 

 ![skype](/home/mrzizik/screenshots/skype.png)

 ![skype_chat](/home/mrzizik/screenshots/skype_chat.png)



 ![skype_contact](/home/mrzizik/screenshots/skype_contact.png)



11:30 - At last go to browser's cache.

In mozilla's cache we have some interesting images of map (Paris, Berlin, Naples, New York) and driver's site screenshot. Let's start from drivers. Looking on them we can suppose that suspect has Lenova IdeaPad notebook.

 ![ideapad](/home/mrzizik/screenshots/ideapad.png)

Also suspect tried to find some place to stay in several cities. New York mosly.

 ![NewYork](/home/mrzizik/screenshots/NewYork.png)



Here we have list of visited sites from Mozilla and IE.

 ![IEhist](/home/mrzizik/screenshots/IEhist.png)

 ![IEhistmk](/home/mrzizik/screenshots/IEhistmk.png)

 ![Mozillahistjb](/home/mrzizik/screenshots/Mozillahistjb.png)