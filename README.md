

***Predicting drug sensitivity from genetic screens in cancer cell lines***
------------------------------------------------------------------------




One of the goals of precision medicine in cancer is to identify treatments that will work in molecularly defined cohorts of patients (e.g. patients whose tumour harbours a mutation in gene X will respond well to drug Y). One approach to identifying these associations is to screen existing drugs in panels of cancer cell lines to see which drugs kill which cell lines. By connecting this data with genome sequencing in the cell lines it is possible to associate a particular mutation with increased sensitivity to particular drugs. However, the majority of human genes cannot be inhibited with existing drugs and consequently this approach may miss targets that would be very effective if we developed new drugs for them. An alternative approach is to use loss of function genetic screening to identify genes that different cancer cell lines depend upon for survival. Various experimental techniques (RNA interference, CRISPR screening) can be used to inhibit individual genes and measure how this impacts cell line  growth. In recent years very large scale efforts have been performed to measure the sensitivity of hundreds of cancer cell lines to either collections of drugs or to collections of gene targetting reagents. A comprehensive evaluation of the relationship between the two data types has yet to be performed. Theoretically loss-of-function genetic screens should provide sufficient information to predict the results of drug sensitivity screens. If a drug targets the function of a specific gene, and we know that inhibiting that gene kills a specific cell line, then we could predict that the drug should also kill the cell line. However, things are rarely that straightforward - many drugs will inhibit the function of multiple genes, while for some drugs we do not know which genes they inhibit. The goal of this project is to assess how accurately we can predict drug sensitivity from genetic screens.

***Core:***
Loss of function screen datasets and drug sensitivity datasets will be provided

•	For drugs with known target genes, quantify how well the gene    inhibition measurements predict    drug sensitivity measurements

•	For all drugs, apply a machine learning approach (e.g. random forest regression) to predict    the sensitvity of cell lines to that drug by using the loss-of-function screens as input features

•	Analyse the relationship    between feature importance (as determined by the machine learning    model)    and reported drug targets (e.g. is the reported target gene of a drug always the most important feature,    if two genes are targetted by a drug are both identified as important features)

***Advanced:***

 - •	Compare the predicitive power derived from loss-of-function screens  to that derived from other source (e.g. gene expression)
 - •	Assess the robustness of the predictive models by testing predictions on additional

