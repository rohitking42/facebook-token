### GitHub Par Upload Kaise Kare (Termux Se)

Agar tune files bana li hain, toh bas ye commands maar Termux mein upload karne ke liye:

1.  GitHub pe jaake **New Repository** bana (Naam: `FB-Cookie-To-Token`).
2.  Fir Termux mein aake jaha files hain waha ye commands laga:

```bash
git init
git add .
git commit -m "First upload"
git branch -M main
git remote add origin https://github.com/TeraGithubUsername/FB-Cookie-To-Token.git
git push -u origin main
