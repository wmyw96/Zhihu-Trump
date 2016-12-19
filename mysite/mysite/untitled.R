library(ggplot2)
library(scales)
paths = read.csv("temp.csv",header = FALSE,sep = ",")
if (length(paths$V1) == 2)
{
	dat_line = read.csv(paths$V2[1],header = FALSE,sep = ",")
	dat_line$V1 = as.Date(dat_line$V1)
	gg = ggplot(dat_line,aes(x = V1,y = V2,group = 1)) + geom_line() + scale_x_date(labels = date_format("%y-%m-%d")) + labs(x = "Date", y = "Count")
	ggsave("static/myplot_line.jpg",gg)
	dat_density = read.csv(paths$V2[2],header = FALSE,sep = ",")
	dat_density$V1 = as.Date(dat_density$V1)
	gg = ggplot(dat_density,aes(V1)) + geom_density(alpha = .1,fill = "blue",color = "blue") + labs(x = "Date", y = "Density")
	ggsave("static/myplot_density.jpg",gg)
}
else
{
	dat_line_1 = read.csv(as.character(paths$V2[1]),header = FALSE,sep = ",")
	dat_line_2 = read.csv(as.character(paths$V2[3]),header = FALSE,sep = ",")
	dat_line_1$V1 = as.Date(dat_line_1$V1)
	dat_line_2$V1 = as.Date(dat_line_2$V1)
	gg = ggplot() + geom_line(data = dat_line_1,aes(x = V1,y = V2,group = 1),color = "red") + geom_line(data = dat_line_2,aes(x = V1,y = V2,group = 1),color = "blue") + scale_x_date(labels = date_format("%y-%m-%d"))+
	 labs(x = "Date", y = "Count")
	ggsave("static/myplot_line.jpg",gg)
	dat_density_1 = read.csv(as.character(paths$V2[2]),header = FALSE,sep = ",")
	dat_density_2 = read.csv(as.character(paths$V2[4]),header = FALSE,sep = ",")
	dat_density_1$V1 = as.Date(dat_density_1$V1)
	dat_density_2$V1 = as.Date(dat_density_2$V1)
	gg = ggplot() + geom_density(data = dat_density_1,aes(V1),alpha = .1,fill = "blue",color = "blue") + geom_density(data = dat_density_2,aes(V1),alpha = .1,fill = "green",color = "green") + labs(x = "Date", y = "Density")
	ggsave("static/myplot_density.jpg",gg)
}