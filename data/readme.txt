data4daniel.RDS contains the preprocessed ROSMAP blood monoctype RNA-seq data. To access the data in R, you need to first install & load R package Biobase. Then follow the below example code to extract the data.

library(Biobase)
x = readRDS('data4daniel.RDS')
mat = exprs(x) #Extract the expression data matrix
meta = pData(x) #extract the phenotype data
