# ÉBAUCHE EN ATTENTE DE RÉVISION PROFESSIONNELLE

> Ébauche établie à partir de l'inventaire des données (`INVENTAIRE_DONNEES.md`, §5). Elle ne
> constitue pas un avis juridique et n'est pas publiée : l'application n'y renvoie pas tant que le
> fondateur ne l'a pas approuvée après la révision d'un professionnel du Québec. La version
> française sera obligatoire.
>
> Traduction française de l'ébauche espagnole `docs/legal/COOKIES.md`.

# Politique relative aux témoins de My Idea

**Dernière mise à jour :** [date de publication]

## 1. Ce que nous utilisons et pourquoi

My Idea utilise **uniquement les témoins (cookies) et le stockage local nécessaires au
fonctionnement de l'application** ou à la mémorisation de vos préférences. **Nous n'utilisons aucun
témoin d'analyse, de publicité ou de tiers qui vous suit d'un site à l'autre.**

| nom | type | à quoi il sert | durée |
|---|---|---|---|
| `sb-*` (Supabase) | témoin nécessaire | maintenir votre session ouverte, y compris celle de l'identité invisible qui vous permet d'écrire votre idée sans compte | celle de la session Supabase (À VÉRIFIER) |
| Vérificateur PKCE de Supabase | témoin nécessaire | effectuer la connexion avec Google de façon sécuritaire | quelques minutes (À VÉRIFIER) |
| `post_login_next` | témoin nécessaire | revenir à la page où vous étiez après la connexion | 10 minutes |
| `myidea_idioma` | témoin de préférence | mémoriser la langue que vous avez choisie (activé lorsque l'application est offerte en plusieurs langues) | 1 an |
| `mi-idea:gantt-vista` | stockage local | mémoriser la vue du diagramme de Gantt que vous préférez | jusqu'à ce que vous effaciez les données du navigateur |
| `mi-idea:selector-estado-usado` | stockage local | ne plus vous montrer une indication que vous avez déjà vue | jusqu'à ce que vous effaciez les données du navigateur |

## 2. Votre choix

Les témoins nécessaires ne peuvent pas être désactivés sans que l'application cesse de fonctionner
(par exemple, vous ne pourriez pas maintenir votre session). Vous pouvez effacer les témoins de
préférence et le stockage local à partir des paramètres de votre navigateur; l'application
reviendra alors à ses valeurs par défaut. Si un jour nous utilisions des témoins qui ne sont pas
nécessaires, nous vous demanderions d'abord votre consentement (exigence À VÉRIFIER avec le
professionnel).

## 3. Pour en savoir plus

La façon dont nous traitons vos données est décrite dans la Politique de confidentialité. Pour
toute question, écrivez à privacidad@myideaproject.com.
