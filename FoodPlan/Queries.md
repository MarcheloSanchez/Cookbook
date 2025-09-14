# Shopping list

```dataview
TABLE without id join(ingredients, "<br>") as Ingredients, join(choice(ingredients.Stock, "✔", "❌"), "<br>") as Stock, file.link as Recipe
FROM "Recipe"
where day != null
```


# Recipe

```dataview
table without id file.link as Recipe, Cost, Ingredients
from "Recipe"
```



## Snídaně 

```dataview
table without id file.link as Recipe
from "Recipe"
where Time = breakfast
```


## Obědy

```dataview
TABLE without id file.link as Recipe
FROM "Recipe"
where Time = lunch
```
