library(Biobase)
getwd()
x <- readRDS("./data/data4daniel.RDS")
mat <- exprs(x) #Extract the expression data matrix
meta <- pData(x) #extract the phenotype data