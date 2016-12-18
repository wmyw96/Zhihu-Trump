#This file is used to plot a picture using the generated data
library(ggplot2)
library(scales)
dat = read.csv("temp.csv",header = FALSE,sep = ",")
dat$V1 = as.Date(dat$V1)
gg = ggplot(dat,aes(x = V1,y = V2,group = 1)) + geom_line() + scale_x_date(labels = date_format("%y-%m-%d")) + labs(x = "Date", y = "Count")
ggsave("static/myplot.jpg",gg)