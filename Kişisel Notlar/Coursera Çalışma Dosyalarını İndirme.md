# Coursera Çalışma Dosyalarını İndirme

- Çalışma alanı sayfanıza girin (dosyaların olduğu yer)
- Alttaki komutu kopyalayın
- Tekrar dosyaların olduğu yere gelin ve orada beliren `workspace.tar.gz` dosyasını indirin

```sh
cd ~/work
tar cvfzh ~/workspace.tar.gz *
mv ~/workspace.tar.gz ~/work/workspace.tar.gz
```

**Dosyaların Boyutu 200MB'den Fazla İse**

- Alttaki komutu kopyalayın ve tek tek indirin
- İndirdikten sonra dosyaları `cat workspace.tar.gz.part.* > workspace.tar.gz` ile birleştirebilirsiniz

```sh
split -b 200m workspace.tar.gz workspace.tar.gz.part.
```

> [Downloading all the assignments jupyter notebooks and files](https://www.reddit.com/r/learnmachinelearning/comments/7er5ps/coursera_downloading_all_the_assignments_jupyter/)




