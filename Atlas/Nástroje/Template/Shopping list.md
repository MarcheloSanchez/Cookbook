<%*
const dv = app.plugins.plugins["dataview"].api
-%>
<%*
let dql = await dv.tryQuery(`
TABLE 
FROM "Recipe"
where day
FLATTEN filter(ingredients, (t) => !t.stock) as I
group by I as Ingredients
`)
let tasks = []
for(row of dql.values){
    tasks.push("- [ ] " + row)
}
for(i in tasks){
-%>
<%tasks[i]%>
<%*
}
-%>