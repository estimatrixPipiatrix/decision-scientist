#! /usr/bin/Rscript

library(hdm)
data(cps2012)
cps <- cps2012
write.csv(cps,'pay_gap.csv')
