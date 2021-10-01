# MechaCar_Statistical_Analysis
## Overview
The MecharCar statistical analysis project we perform retrospective analysis on historical vehicle manufacturing data, analytcal verification and validation of current automotive specifications and study design of future product testing. Our analysis will have a statistical backbone, a quantittative metric, and a clear interpretation of the results in order to generate insights to help the production team stay ahead of the competition. To complete our analysis we would perform the following steps:

* Perform multiple linear regression analysis to identify which variables in the dataset predict the mpg of MechaCar prototypes
* Collect summary statistics on the pounds per square inch (PSI) of the suspension coils from the manufacturing lots
* Run t-tests to determine if the manufacturing lots are statistically different from the mean population
* Design a statistical study to compare vehicle performance of the MechaCar vehicles against vehicles from other manufacturers. For each statistical analysis, you’ll write a summary interpretation of the findings.
### Linear Regression to Predict MPG
1. Which variables/coefficients provided a non-random amount of variance to the mpg values in the dataset?
   * From the output of the linear model, we see that vehicle length and ground clearance has the highest impact on predicting mpg with very small p-values, a unit change in any one of these two variables results in a 6.267128 and 3.545534 increase in mpg respectively keeping all other factors constant
2. Is the slope of the linear model considered to be zero? Why or why not?
   * From the equation of the linear model, given as:
  mpg = 6.26713(vl) + 0.00125(vw) + 0.06877(sa) + 3.54553(gc) - 3.41150(AWD) - 103.96398, we see that all coefficients of our predictor varaiables are non-zero, therefore the slope of our linear model is non-zero.
   * The coefficients of our predictor variables is further explained by our correlation matrix where we see very weak to moderate correlation between our predictor variables and mpg
  ##### Correlation Matrix
  ![Correlation_Matrix_mpg](https://user-images.githubusercontent.com/67847583/127755537-b623ed64-e410-432b-bf26-a8b0474c73bc.png)

3. Does this linear model predict mpg of MechaCar prototypes effectively? Why or why not?
   * With very small p-values for vehicle length and ground clearance, our model does a good explaining 75% of the relationship between mpg and the predictor variables. we however notice that the vehicle weight, spoiler angle, and AWD variables do not have statistically significant relationship with mpg, judging from their large p-values.
   * Also, we notice that AWD is binary variable, thus we may want to consider a logistic regression between mpg and AWD.

  ##### Model Summary
  ![Model_Summary_mpg](https://user-images.githubusercontent.com/67847583/127756195-1aa62e23-aac7-4953-baf7-42c9791e0869.png)

### Summary Statistics on Suspension Coils
1. The design specifications for the MechaCar suspension coils dictate that the variance of the suspension coils must not exceed 100 pounds per square inch. Does the current manufacturing data meet this design specification for all manufacturing lots in total and each lot individually? Why or why not?
    * Visually inspecting the total summary, and the lot summary data frames, we see that the total summary variance at 62.29356 is within design specification. Similarly, variances for Lot1 and Lot2 are within design specification. We however notice that Lot3 has a higher than normal variance at 170.2861224
  ##### Total Summary Variance &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Lot Summary Variance
  ![Total_Summary](https://user-images.githubusercontent.com/67847583/127760140-b4c5c799-83a7-4976-8e63-15f705c36f69.png)
  ![Total_Summary](https://user-images.githubusercontent.com/67847583/127760177-be79f2cb-b442-4f16-a518-697dcb297ac0.png)

### T-Tests on Suspension Coils
1. Determine if the PSI across all manufacturing lots is statistically different from the population mean of 1,500 pounds per square inch.
   * Assuming our significance level was the common 0.05 percent, our p-value is above our significance level. Therefore, we do not have sufficient evidence to reject the null hypothesis, and we would state that the two means are statistically similar. 
  
  ##### T-Tests Summary [Sample Mean versus Population Mean]
  ![t_test_All_Lots_vs_Population](https://user-images.githubusercontent.com/67847583/127927867-e1ca64c2-0ab8-43d0-918d-7c798c1fe8f1.png)

 
2. Determine if the PSI for each manufacturing lot is statistically different from the population mean of 1,500 pounds per square inch.
   * Lot 1: Assuming our significance level was the common 0.05 percent, our p-value is above our significance level. Therefore, we do not have sufficient evidence to reject the null hypothesis, and we would state that the two means are statistically similar.

  ##### T-Tests Summary [Lot 1 Mean versus Population Mean]
  ![t_test_Lot1_vs_Population](https://user-images.githubusercontent.com/67847583/127928070-5dd3004e-008a-4430-8a8b-ad3c3e962418.png)


   * Lot 2: Assuming our significance level was the common 0.05 percent, our p-value is above our significance level. Therefore, we do not have sufficient evidence to reject the null hypothesis, and we would state that the two means are statistically similar.

  ##### T-Tests Summary [Lot 2 Mean versus Population Mean]
  ![t_test_Lot2_vs_Population](https://user-images.githubusercontent.com/67847583/127928247-b60c5fc3-5622-4131-9bea-d6f2cc1d3873.png)


   * Lot 3: Assuming our significance level was the common 0.05 percent, our p-value is below our significance level. Therefore, we have sufficient evidence to reject the null hypothesis, and we would state that the two means are not statistically similar.

  ##### T-Tests Summary [Lot 3 Mean versus Population Mean]
  ![t_test_Lot3_vs_Population](https://user-images.githubusercontent.com/67847583/127928375-bc5b3612-e636-4996-870b-264d2d06891d.png)

## Study Design: MechaCar vs Competition.
Since our study design seeks to improve MecharCar against competition, we would look to study metrics such as cost, city or highway fuel efficiency, horse power, maintenance cost, or safety rating.
1. Research Question
   - Are there differences average city or highway fuel effiency between MecharCar vehicles and competition vehicles?
2. Forming Our Hypothesis
   - Null Hyothesis: There is no difference between average city or highway fuel efficiency between MecharCar and Competition vehicles
   - Alternative Hypothesis: There is difference between average city or highway fuel efficiency between MecharCar and Competition vehicles
3. Statistical Test
   - Since we are dealing with dichotomous data, (sample A vs Sample B), and our dependent variable (city or highway fuel efficiency) is continous, we would employ the Two-sample t-test to evaluate if there are differences in fuel effieciency between MecharCar and competition vehicles
4. Data Requirement
   - Sample A: sufficiently large MecharCar sample data set of fuel efficiency
   - Sample B: sufficiently large competition sample data set of fuel efficiency
