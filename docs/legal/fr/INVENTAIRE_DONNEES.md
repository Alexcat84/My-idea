# Inventaire des renseignements personnels de My Idea

> Traduction française de l'inventaire espagnol `docs/legal/INVENTARIO_DATOS.md`. Les noms de
> tables, de fichiers, de colonnes et de variables du code sont laissés tels quels.

**Date :** 26 septembre 2026. **Base :** lecture du code (`web/`, `engine/`) et des 44 migrations de
`supabase/migrations/`, sur la branche `i18n` (`main` à `dc5f5e65`). Ce que le code ne permet pas
d'affirmer porte la mention **À VÉRIFIER**. Cet inventaire sert de base aux ébauches des
Conditions d'utilisation, de la Politique de confidentialité et de la Politique relative aux
témoins de ce dossier.

## 1. Ce qui est conservé et où

Tout se trouve dans la base de données **Supabase** (PostgreSQL et authentification). Sauf
indication contraire, chaque table est rattachée au compte avec `ON DELETE CASCADE` (elle est
supprimée avec le compte), directement ou par l'intermédiaire de `projects`.

| donnée | table ou emplacement | contenu |
|---|---|---|
| Compte | `auth.users` (géré par Supabase) | adresse courriel, hachage du mot de passe ou identité Google, dates; dans `app_metadata`, les identités invisibles en attente d'adoption |
| Identité invisible (visiteur) | `auth.users` anonyme, créé lors de la première visite (`proxy.ts`) | un identifiant sans adresse courriel; les idées écrites avant la création d'un compte y sont rattachées jusqu'à leur adoption |
| Idées | `projects` | le texte original de l'idée tel qu'il a été écrit ou dicté, le titre, le résumé évolutif généré par l'IA, le type d'offre, le motif de clôture |
| Réponses à l'entretien | `sessions` | message d'entrée, état du parcours (l'historique de la conversation et les chiffres détectés), registre des décisions du moteur, qualité, coût de l'IA |
| Plans et documents | `plans`, `project_unlocks` (diagnostics de monde), `project_actas` (instantanés de la clôture) | le plan sous forme de texte, les diagnostics, les instantanés du bilan de clôture |
| Tâches et notes | `checklist_items` | le texte de chaque tâche, les notes de l'utilisateur, le motif de mise de côté d'une tâche, les dates, les champs de protection |
| Journal de bord | `project_bitacora` | les événements correspondant aux décisions de l'utilisateur (avec un `payload` libre) |
| Chiffres de l'entreprise | `projects.numeros_proyecto`, `project_numeros_versiones` | coûts, heures, prix, frais fixes, ventes, avec le texte écrit par l'utilisateur; chaque version du tableau et sa narration |
| Parcours dans le graphe | `project_nodes`, `node_visits`, `project_modos` | les concepts travaillés; le mode et la capacité de chaque espace |
| Crédits | `credit_accounts`, `credit_transactions`, `credit_reservas`, `query_credits` (ancienne), `beta_courtesy_log` | solde, mouvements (prélèvements, attributions, remboursements), réservations en cours |
| Remboursements | `credit_refund_log` | identifiant d'utilisateur, montant et motif. **Sans clé étrangère vers le compte : survit à la suppression** (constat B1) |
| Événements de paiement | `revenuecat_webhook_events` | identifiant d'utilisateur du processeur, type d'événement. **Sans clé étrangère : survivrait à la suppression** (constat B2). Aucun code ne l'alimente aujourd'hui |
| Vérification en deux étapes | `user_seguridad` (secret TOTP chiffré en AES-256-GCM), `two_factor_recovery_codes` (hachage bcrypt), `two_factor_email_codes` (hachage, expire après 10 min), `two_factor_attempts` | secrets chiffrés, codes hachés, **adresse IP** et session de chaque tentative |
| Liste des invités de la version bêta | `beta_allowlist` | **l'adresse courriel en clair**, la personne qui a invité et des notes. **Sans lien avec le compte : survit à la suppression** (constat B3) |
| Empreinte anti-abus de la courtoisie | `cortesia_email_log` | le hachage SHA-256 de l'adresse courriel. Sans lien avec le compte **à dessein** : empêche que la suppression puis la recréation du compte répète la courtoisie (la courtoisie est aujourd'hui inactive) |
| Clics sur les mondes | `pack_clicks` | identifiant d'utilisateur et monde |
| Google Agenda | `google_calendar_cuenta` (jeton chiffré, adresse courriel Google), `google_calendar_evento` | tables créées (migration 031) **sans aucun code qui les utilise** |
| Calendrier par abonnement | le flux `/api/calendar/feed/<token>.ics` | transmet les noms des idées et le texte des tâches datées à l'application de calendrier de l'utilisateur; le jeton est un HMAC de l'identifiant d'utilisateur |
| Limites d'utilisation | **Upstash Redis** | clés contenant l'**adresse IP** ou l'identifiant d'utilisateur : limite quotidienne (24 h), coupe-circuit global (48 h), envois de code de vérification en deux étapes (10 min) |
| Journaux du serveur | **Vercel** (journaux) | certaines lignes contiennent des identifiants d'utilisateur et des adresses courriel (par exemple, l'adresse courriel d'une tentative de connexion d'une personne non invitée) |

## 2. Pendant combien de temps

- **Tant que le compte existe**, tout ce qui figure au §1. Il n'y a aucun nettoyage périodique
  (aucune tâche cron, `vercel.json` sans tâche planifiée).
- **Selon une durée :** Upstash jusqu'à 48 h; codes de vérification en deux étapes par courriel
  10 min (les codes utilisés restent); le témoin de retour après la connexion 10 min.
- **Identités invisibles et leurs idées non adoptées :** pour toujours jusqu'à la correction
  `borrado-cuenta`; avec celle-ci, elles sont supprimées après 30 jours d'inactivité.
- **Après la suppression du compte :** voir le §4.
- **Copies de sauvegarde de Supabase et conservation des journaux de Vercel :** À VÉRIFIER
  (dépendent du forfait souscrit).

## 3. À qui les données sont transmises (fournisseurs)

| fournisseur | fonction | ce qu'il reçoit | pays |
|---|---|---|---|
| **Anthropic** (Claude) | rédiger l'entretien, la Clarté, le plan, les diagnostics, les chiffres commentés | le texte de l'idée, les réponses, le résumé évolutif, les chiffres de l'entreprise | À VÉRIFIER (probablement les États-Unis) |
| **Voyage AI** | recherche sémantique dans le graphe (plongements vectoriels) | le texte des réponses, le profil de la session ou l'idée originale, à chaque tour | À VÉRIFIER (probablement les États-Unis) |
| **Supabase** | base de données et authentification | tout ce qui figure au §1 | À VÉRIFIER (région du projet dans le tableau de bord de Supabase) |
| **Vercel** | hébergement et exécution de l'application | toutes les requêtes; journaux contenant des identifiants et des adresses courriel | À VÉRIFIER (probablement les États-Unis; région des fonctions dans le tableau de bord) |
| **Resend** | courriel du code de vérification en deux étapes et, selon `.env.example`, le SMTP des courriels de Supabase | l'adresse courriel de l'utilisateur et le code | À VÉRIFIER (probablement les États-Unis) |
| **Upstash** | limites d'utilisation | l'adresse IP ou l'identifiant d'utilisateur contenus dans les clés | À VÉRIFIER (région de la base de données) |
| **Google** | connexion avec Google (OAuth, par l'intermédiaire de Supabase) | l'identité Google de l'utilisateur qui choisit cette méthode | À VÉRIFIER (probablement les États-Unis) |
| **Processeur de paiement** | encaisser l'achat de crédits | rien pour l'instant : l'achat avec de l'argent n'est pas activé (un schéma est prévu pour RevenueCat, sans code ni clés) | À VÉRIFIER lors de son activation |

- **Polices de caractères :** `next/font/google` télécharge la police au moment de la construction
  de l'application et la sert depuis notre domaine, de sorte que le navigateur n'interroge pas
  Google pour l'obtenir (À VÉRIFIER dans le déploiement).
- **Aucun outil d'analyse ni publicité de tiers :** ni Vercel Analytics, ni PostHog, ni Sentry, ni
  pixels.
- **Si un fournisseur utilise les données pour entraîner ses modèles :** À VÉRIFIER dans sa
  politique (liens dans l'ébauche de la Politique de confidentialité). Le code ne permet pas de
  l'affirmer.

## 4. La suppression du compte (vérifiée dans le code)

`/api/cuenta/eliminar` exige le mot « ELIMINAR » (et la vérification en deux étapes si elle est
activée), conserve au besoin l'empreinte anti-abus de la courtoisie, puis appelle
`auth.admin.deleteUser`. **Tout le reste dépend du `ON DELETE CASCADE`.** Sont supprimés avec le
compte : les idées, les sessions, les plans, les tâches, le journal de bord, les chiffres, les bilans
de clôture, le solde de crédits, les réservations et les données de vérification en deux étapes.

**Ce qui survivait à la suppression (constats B1 à B4). CORRIGÉ et en production (décisions du
fondateur, 26 septembre 2026; `main` 8d890b3e, web-v2.6.9, migration 044 appliquée) :**
B3 et B4 sont supprimés; B1 et B2 sont anonymisés (le montant et la date subsistent); les idées
d'invités sans propriétaire sont supprimées automatiquement après 30 jours d'inactivité (tâche
planifiée quotidienne). Ce qui a été constaté :
- **B1.** `credit_refund_log` : identifiant d'utilisateur, montant et motif.
- **B2.** `revenuecat_webhook_events` : l'identifiant d'utilisateur du processeur (aucune ligne
  aujourd'hui).
- **B3.** `beta_allowlist` : l'adresse courriel en clair, avec la personne qui a invité et des notes.
- **B4.** Les identités invisibles en attente d'adoption et **les idées écrites avant la
  connexion**.

**Ce qui survit et est déclaré, sans constituer un défaut :**
- L'empreinte hachée de l'adresse courriel dans `cortesia_email_log`, à dessein (fondement juridique
  À VÉRIFIER).
- Les clés d'Upstash, jusqu'à 48 h.
- Les journaux de Vercel, selon leur durée de conservation.
- Les copies déjà transmises à Anthropic, à Voyage et à Resend, selon leurs politiques.

**B5, historique de crédits (décision du fondateur, 27 septembre 2026) :** le `ON DELETE CASCADE`
de `credit_transactions` emportait l'historique complet. Il demeure désormais **anonyme**, comme B1
et B2 : le montant (`delta`, avec son `tipo` : achat, consommation ou remboursement) et la date;
`user_id`, `saldo_resultante`, `concepto`, `origen` et `idempotency_key` sont mis à NULL avant la
suppression du compte (migration 045, `main` ad8b2059, web-v2.6.10). **Les registres fiscaux des
ventes sont conservés par le processeur de paiement.**

## 5. Navigateur

- **Témoins de Supabase** (`sb-*`) : la session, y compris celle de l'identité invisible; et le
  vérificateur PKCE lors de la connexion avec Google.
- **`post_login_next` :** la page où revenir après la connexion (httpOnly, 10 min).
- **localStorage :** `mi-idea:gantt-vista` (vue préférée du diagramme de Gantt) et
  `mi-idea:selector-estado-usado` (une indication déjà vue).
- **Prochainement (i18n, F2) :** `myidea_idioma`, la langue préférée.

## 6. La dictée

`web/lib/useSpeech.ts` utilise uniquement la reconnaissance vocale du navigateur
(`SpeechRecognition`). L'application n'enregistre ni ne téléverse aucun son. Le texte dicté s'inscrit
dans le champ et est transmis comme du texte écrit. L'endroit où le navigateur lui-même traite le son
(par exemple, sur les serveurs du fabricant) : À VÉRIFIER, et cela dépend du navigateur.

## 7. Tout ce qui est À VÉRIFIER

1. Le pays et la région de chaque fournisseur (§3), dans leurs tableaux de bord et leurs contrats.
2. Si Anthropic, Voyage, Supabase, Vercel, Resend, Upstash ou Google utilisent les données pour
   entraîner des modèles ou à d'autres fins; et leurs délais de conservation.
3. La conservation des copies de sauvegarde de Supabase et des journaux de Vercel.
4. Le processeur de paiement, lorsqu'il sera activé.
5. Le fondement juridique de la conservation de l'empreinte hachée de la courtoisie après la
   suppression.
6. ~~S'il existe une obligation de conserver les registres des transactions~~ RÉSOLU par décision
   du fondateur (27 septembre 2026) : l'historique demeure anonyme et les registres fiscaux des
   ventes sont conservés par le processeur de paiement (§4, B5).
7. L'endroit où le navigateur traite le son lors de la dictée.
8. Que `next/font` n'interroge pas Google dans le déploiement réel.
9. ~~Le nom légal~~ CONFIRMÉ par le fondateur selon ses certificats de Revenu Québec :
   **Alexis Garcia Hurtado** (entreprise individuelle, sans second prénom); TPS/TVH
   72180 8434 RT0001 et TVQ 4056093040 TQ0001, en vigueur depuis le 7 avril 2026. Coordonnées :
   privacy@myideaproject.com (protection des renseignements personnels et droits des utilisateurs) et
   support@myideaproject.com (soutien général). **L'adresse du commerçant reste À VÉRIFIER** : la Loi
   sur la protection du consommateur du Québec l'exige généralement dans les contrats conclus à
   distance; le fondateur décidera avec le professionnel de publier une adresse d'affaires ou une case
   postale.
