# Data Challenge: Intern Test Questions

This challenge uses a dataset generated to simulate user journeys on a website. Please answer the following questions based on the provided schema. You may develop the solutions within a Python script or Notebook, for SQL queries consider using the SQLite package.

**Dataset Schema:**

* **`ad_clicks`**: `click_id`, `impression_id`, `user_id`, `ad_id`, `timestamp`, `click_source_url`
* **`ad_impressions`**: `impression_id`, `user_id`, `ad_id`, `timestamp`, `page_url`, `campaign_id`
* **`order_items`**: `order_id`, `order_item_id` (sequential per order), `product_id`, `quantity`, `price_per_unit`
* **`orders`**: `order_id`, `user_id`, `order_date` (timestamp), `total_amount`, `currency`, `exchange_rate_to_eur`, `status`, `shipping_address`
* **`page_views`**: `view_id`, `user_id`, `session_id`, `page_url`, `timestamp`, `device_type`, `browser`, `website_locale`
* **`products`**: `product_id`, `product_name`, `category`, `price`, `stock_quantity`, `date_added`, `base_view_probability`
* **`users`**: `user_id`, `first_name`, `last_name`, `email`, `registration_date`, `last_login_date`, `country`, `website_locale`, `user_segment`

---

**Section 1: SQL & Data Retrieval**

1.1. Write a SQL query to find the top 10 most frequently purchased products, listed by their `product_name` and total quantity sold.

1.2. Write a SQL query to identify users (list their `user_id` and `email`) who registered in the last 6 months but have not placed any orders.

1.3. Write a SQL query to calculate the average number of page views per session for each `device_type`.

1.4. Write a SQL query to determine the overall click-through rate (CTR) for all ads. CTR is defined as (Total Clicks / Total Impressions) * 100.

(Optional) 1.5. Write a SQL query to find the month-over-month growth rate of the total sales amount. The output should show `year`, `month`, `total_sales_for_month`, and `mom_growth_rate`.

(Optional) 1.6. Write a SQL query to find the average time (in days) between a user's `registration_date` and their first `order_date`. Consider only users who have placed at least one order.

(Optional) 1.7  Write a SQL query to identify the most viewed product category. (Assume product views are based on page views).

Note - Consider visualising the results of these queries.
---

**Section 2: Data Analysis & Interpretation**

2.1. Describe how you would approach an analysis to understand the customer journey from the first ad impression to a purchase. Which tables are key, and what steps would you take?

2.2. The `users` table has a `user_segment` column (e.g., 'casual', 'engaged', 'researcher'). How could a company use this segmentation to improve its business?

---

**Section 3: Data Modeling - Simple Regression Task**

3.1. Your goal is to build a **simple regression model** to predict the `total_amount` of an order.

    a.  **Objective:** Clearly state the specific regression problem you are trying to solve.
    b.  **Feature Selection:**
        * Identify features from the provided schema (you might need to derive some from existing columns or join tables) that you believe would be good predictors for `total_amount`.
        * Explain your reasoning for choosing each feature.
    c.  **Data Preparation:** Briefly describe the key steps you would take to prepare the data for your chosen features (e.g., handling missing values, encoding categorical variables if any, scaling).
    d.  **Model Choice:**
        * Which **regression algorithm** would you choose for this task?
        * Why is this model appropriate as a starting point?
    e.  **Evaluation:** How would you evaluate the performance of your regression model?
    f.  * Is this specific regression case relevant? Why is it, or why is it not?
