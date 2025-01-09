

df_cellcounts <- data.frame(
                    cell1=round(runif(3)*10), cell2=round(runif(3)*10), cell3=round(runif(3)*10), 
                    row.names=c('gene1', 'gene2', 'gene3'))

# normalize counts
apply(df_cellcounts, 1, FUN= function(x){round(x/sum(x)*100)})
apply(df_cellcounts, 2, FUN= function(x){round(x/sum(x)*100)})