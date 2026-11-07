# zipsoft.fr

Le site de David "Zip" Pierron : https://zipsoft.fr, en français à la racine et en anglais sous `/en/`.
Une page d'accueil qui présente toutes les réalisations (jeux, outils pour DCS World, applications, puis les projets auxquels je contribue), le contact et les mentions légales.

## Construire

Le site est construit avec [Hugo](https://gohugo.io) 0.168.0, sans thème ni dépendance.

```bash
hugo server                        # aperçu sur http://localhost:1313
hugo --minify --panicOnWarning     # le site construit, dans public/
```

## Ajouter une réalisation

Une réalisation est un fichier par langue : `content/fr/realisations/<nom>.md` et `content/en/realisations/<nom>.md`, au même nom.

```yaml
---
title: "Nom du projet"
weight: 13                  # l'ordre dans sa catégorie
category: dcs               # games, dcs ou apps
role: author                # author ou contributor
org: "VEAF"                 # facultatif
image: "img/projet.png"     # une image dans assets/img/ (capture réduite par Hugo, ou SVG tel quel)
links:
  site: "https://…"         # facultatifs, dans cet ordre : site, docs, code
  code: "https://github.com/…"
---

Deux lignes de présentation, une phrase par ligne.
```

Un projet n'a pas de page à lui : il n'apparaît que comme fiche, sur l'accueil, et toutes les fiches y sont.
Les projets `author` sont dans « Mes réalisations », rangés par catégorie (jeux, DCS, applications) puis par `weight` (une catégorie inconnue arrête la construction) ; les `contributor` (les projets d'autres auxquels je participe) ont leur propre partie, « Mes contributions », à la fin.
Le dossier `realisations/` ne sert qu'à ranger les fiches : il n'est pas construit en page, et ses anciennes adresses (`/realisations/`, `/en/projects/`) redirigent vers l'accueil de leur langue.
Un projet sans capture d'écran reçoit une illustration dessinée : sa couverture s'ajoute dans `tools/covers.py`, puis `python tools/covers.py assets/img/covers` les redessine toutes.

## Le style

Les polices du système (rien n'est chargé depuis un autre site), une couleur d'accent, un mode sombre qui suit le réglage du système : tout est dans `assets/css/main.css`.

## Déployer

`.github/workflows/deploy.yml` construit le site sur chaque PR, et à chaque poussée vers `main` (ou à la demande) le copie par `rsync` sur le VPS zipsoft, dans `/srv/docker/zipsoft-site/public`.
La clé de déploiement (secret `DEPLOY_KEY`) n'ouvre sur le serveur que `rrsync` dans ce dossier ; sans le secret, le workflow construit le site et dit qu'il ne l'a pas envoyé.

Sur le VPS :

- `/srv/docker/zipsoft-site/compose.yaml` ← `server/compose.yaml` : un conteneur `caddy:2`, `zipsoft-site`, sur le réseau `proxy`.
- `/srv/docker/zipsoft-site/Caddyfile` ← `server/Caddyfile` : il sert `./public` en HTTP, avec la page 404 de chaque langue.
- Dans le Caddyfile principal (`/srv/docker/caddy/Caddyfile`), le domaine et sa redirection :

  ```
  zipsoft.fr {
  	reverse_proxy zipsoft-site:80
  }

  www.zipsoft.fr {
  	redir https://zipsoft.fr{uri} permanent
  }
  ```

  puis `docker exec caddy caddy reload --config /etc/caddy/Caddyfile`.
- La clé de déploiement, sur sa propre ligne de `~david/.ssh/authorized_keys` :

  ```
  command="rrsync /srv/docker/zipsoft-site/public",restrict ssh-ed25519 AAAA… zipsoft-site-deploy
  ```

## Licence

Les textes et la mise en page : tous droits réservés, David "Zip" Pierron.
Chaque projet présenté garde sa propre licence, indiquée dans son dépôt.
