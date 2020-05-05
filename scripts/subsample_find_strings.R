sub<-rownames(subsample[[1]])
gsub("\"","",sub, fixed = TRUE )

subset1<- subset(emb_df, rownames(emb_df) %in% rownames(subsample[[1]]))
subset2<- subset(emb_df, rownames(emb_df) %in% rownames(subsample[[2]]))
subset3<- subset(emb_df, rownames(emb_df) %in% rownames(subsample[[3]]))
subset4<- subset(emb_df, rownames(emb_df) %in% rownames(subsample[[4]]))


icd<-read.csv("diag.csv")
head(icd)

Group1<-as.data.frame(unique(icd[icd$icd10 %in% subset1$Source, "diagnosisstring"]))
Group2<-as.data.frame(unique(icd[icd$icd10 %in% subset2$Source, "diagnosisstring"]))
Group3<-as.data.frame(unique(icd[icd$icd10 %in% subset3$Source, "diagnosisstring"]))
Group4<-as.data.frame(unique(icd[icd$icd10 %in% subset4$Source, "diagnosisstring"]))


length(unique(icd$diagnosisstring))

colnames(Group1)<-c("Diagnosis String")


write.csv(Group1, file = "Output/Group1.csv")
write.csv(Group2, file = "Output/Group2.csv")
write.csv(Group3, file = "Output/Group3.csv")
write.csv(Group4, file = "Output/Group4.csv")
