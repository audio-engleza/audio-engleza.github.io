# 🚀 Ghid de Deployment pe GitHub Pages

## Pasul 1: Crearea Repository-ului

1. Mergeți la [GitHub.com](https://github.com) și faceți login
2. Apăsați butonul verde **"New"** pentru un repository nou
3. Nume repository: `lectii-engleza-varstnici` (sau orice nume doriți)
4. Bifați **"Public"** (necesar pentru GitHub Pages gratuit)
5. Bifați **"Add a README file"**
6. Apăsați **"Create repository"**

## Pasul 2: Upload Fișierelor

### Opțiunea A: Prin Web Interface (Simplu)

1. În repository-ul nou, apăsați **"uploading an existing file"**
2. Trageți toate fișierele din folder-ul `web/` în browser:
   - `index.html`
   - `README.md`
   - `audio/` (tot folder-ul cu toate mp3-urile)
3. Scrieți în commit message: `Adăugare lecții audio de engleză`
4. Apăsați **"Commit changes"**

### Opțiunea B: Prin Git (Avansat)

```bash
# Clonează repository-ul
git clone https://github.com/USERNAME/lectii-engleza-varstnici.git
cd lectii-engleza-varstnici

# Copiază fișierele
cp -r /path/to/web/* .

# Adaugă și commit
git add .
git commit -m "Adăugare lecții audio de engleză"
git push origin main
```

## Pasul 3: Activarea GitHub Pages

1. În repository, mergeți la **Settings** (tab-ul de sus)
2. Scroll down până la secțiunea **"Pages"** din meniul stâng
3. La **"Source"**, selectați **"Deploy from a branch"**
4. La **"Branch"**, selectați **"main"**
5. Lăsați folder-ul pe **"/ (root)"**
6. Apăsați **"Save"**

## Pasul 4: Accesarea Site-ului

După ~5-10 minute, site-ul va fi disponibil la:
```
https://USERNAME.github.io/lectii-engleza-varstnici
```

Înlocuiți `USERNAME` cu numele vostru de utilizator GitHub.

## 🔧 Troubleshooting

### Problemă: Audio-ul nu se redă
- **Cauza**: Fișierele MP3 sunt prea mari pentru GitHub
- **Soluție**: Folosiți un serviciu de hosting audio separat sau comprimați fișierele

### Problemă: Site-ul nu se actualizează
- **Cauza**: Cache-ul browserului
- **Soluție**: Apăsați `Ctrl+F5` (Windows) sau `Cmd+Shift+R` (Mac)

### Problemă: 404 Error
- **Cauza**: GitHub Pages nu e activat corect
- **Soluție**: Verificați din nou Settings → Pages

## 📱 Testare

După deployment, testați pe:
- ✅ Computer desktop
- ✅ Tabletă 
- ✅ Telefon mobil
- ✅ Difuzoare/căști

## 🎯 Customizare

Pentru a adăuga lecții noi:
1. Generați noi fișiere MP3 cu sistemul Ruby
2. Copiați-le în folder-ul `audio/`
3. Editați `index.html` și adăugați noi carduri de lecții
4. Upload pe GitHub

---

💡 **Sfat**: Păstrați fișierele MP3 sub 25MB fiecare pentru GitHub Pages