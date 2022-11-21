todo <- read.csv("todo.lst",strings=F)
currentPoints <- sum(todo$importance[which(todo$complete)])
totalPoints   <- sum(todo$importance)
library(ggplot2)

percentile <- (currentPoints/totalPoints)*100.0

jpeg("statusPlot.jpg",height=200,width=400)
plt <- ggplot() +
  geom_col(aes("", 100),width=0.2) +
  geom_col(aes("", percentile), fill = "forestgreen",width=0.2) +
  coord_flip() +
  theme(axis.title.x=element_blank(),axis.title.y=element_blank())
print(plt)
