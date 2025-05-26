import streamlit as st
from pages import section3_processing, section3_exploration

def render():
    with st.container():
        st.header("Section 3: Data Modeling - Simple Regression Task")

    with st.expander("a. Objective"):
        st.markdown("""
            ### Objective:
            Predict the total_amount (the total value in original currency) of an order at the time the order is placed, based on available features about the user, products, and order context.
            The target variable is `total_amount`, from the order's table.
            The model should be able to predict the total order value using features from the `users`, `orders`, and `products` tables.
        """)
    with st.expander("b. Feature Selection"):
        st.markdown("""
            ### Feature Selection:
                    
            - **User Features**: 
                - `country`: Users from different regions might spend differently. 
                    - I chose this feature rather than `website_locale` because it provides a better insight into market behavior in the regional context.
                - `user_segment`: Indicates the type of user, which could impact spending behavior.
                    
            - **Page Views Features*:
                - `device_type`: Different devices may lead to different user experiences and spending behaviors.
            
            - **Order Items Features**:
                - `quantity`: The number of items in the order, which directly influences the total order value.
                - `price_per_unit`: The price of each item, which is crucial for calculating the total order value.
            
            - **Products Features**:
                - `product_category`: Some categories may correlate with higher order values.
            
            - **Derived Features**:
                - `conversion_lag`: The time difference between the registration date and the order date, which can indicate how long it took for a user to make their first purchase.
                    - Obtained by dividing the difference between `order_date` and `registration_date`.
                    - A shorter lag may indicate higher intent, and thus potentially higher total order values.
        """)

    with st.expander("c. Data Preparation"):
        st.markdown("""
            ### Data Preparation:
            - **Data Cleaning**: 
                - Handle missing values: Ideally using stochastic regression imputation for continuous numerical features (e.g. `price_per_unit`), and mode based for categorical ones.
                - Remove outliers that could skew the model.
                - Anonymize personal information to comply with privacy regulations.
                - Ensure that timestamps are in a consistent format.
            - **Feature Engineering**:
                - Create the `conversion_lag` feature as described above.
                - Convert categorical variables like `country`, `user_segment`, and `product_category` into numerical representations using one-hot encoding.
                - Join the `users`, `orders`, and `products` tables to create a comprehensive dataset that includes all relevant features for each order.
            - **Normalization**:
                - Normalize numerical features (e.g., `quantity`, `price_per_unit`) to ensure they are on a similar scale, which can improve model performance.
            - **Data Splitting**:
                - Split the dataset into training and testing sets to evaluate model performance.
            - **Exploration**:
                - Perform exploratory data analysis (EDA) to understand the distribution of features and their relationships with the target variable (`total_amount`).
                - Visualize correlations between features and the target variable to identify potential predictors.
        """)
    
    with st.expander("d. Model Choice"):
        st.markdown("""
            ### Model Choice:
            - **Linear Regression**: 
                - A simple yet effective model for predicting continuous outcomes like `total_amount`.
                - It assumes a linear relationship between the features and the target variable, which is suitable for this task.
                - Easy to implement and interpret, making it a good starting point for regression tasks.
        """)

    with st.expander("e. Model Evaluation"):
        st.markdown("""
            ### Model Evaluation:
            - **Metrics**:
                - **Mean Absolute Error (MAE)**: Measures the average magnitude of errors in a set of predictions, without considering their direction.
                - **Mean Squared Error (MSE)**: Measures the average of the squares of the errors, giving more weight to larger errors.
                - **R-squared**: Indicates the proportion of variance in the dependent variable that can be explained by the independent variables.
            - **Validation**:
                - Use cross-validation (k-fold) to ensure that the model generalizes well to unseen data.
                - Evaluate the model on the test set to assess its performance and adjust hyperparameters if necessary.
            - **Visualizations**:
                - Plot predicted vs. actual values to visually assess the model's performance.
                - Residual plots to check for patterns in the errors, which can indicate issues with the model.
                - Feature importance analysis to understand which features contribute most to the predictions.
        """)

    with st.expander("f. Relevance"):
        st.markdown("""
            ### Relevance to Business:
                This regression model is highly relevant to the business for several reasons:
                    - The model can help identify which user features (e.g., country, segment) are most predictive of higher order values, providing insights into user behavior and preferences.
                    - It can make accurate predictions of total order values can help in revenue forecasting and financial planning.
                    - Understanding which user segments and product categories lead to higher order values can inform targeted marketing strategies.
                    - Predicting order values can help in managing inventory levels more effectively, ensuring that popular products are always in stock.
                    - Insights from the model can guide improvements in the user experience, such as optimizing the checkout process or personalizing product recommendations.
        """)

    section3_processing.render()

    section3_exploration.render()

render()