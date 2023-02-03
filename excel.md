# Excel

## Cumulative sum in table
```
=SUM(INDEX([ColName],1):[@ColName])
```


## Filtered SharePoint list via Power Query
```
= OData.Feed("https://xxxxx.sharepoint.com/sites/xx/xxxx/_vti_bin/listdata.svc/Timesheets?$filter=Title eq 'Project 1' or Title eq 'Project 2'&$select=Title,Hours,Date,Person", null, [Implementation="2.0"])
```
