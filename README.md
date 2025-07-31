
#  Understanding What Sells: How Data Reveals Customer Choices and Pricing Impact in Food Retail

##  Introduction
In today’s competitive retail landscape, understanding customer behavior and product performance is crucial for driving growth and optimizing strategy. This project dives into transactional food sales data to uncover key insights around sales dynamics, pricing patterns, and regional preferences. Through a combination of exploratory data analysis and focused visualizations, we extract meaningful trends that help explain what sells, where, and why.

##  Objective
- Analyze food sales data to assess category and product performance.
- Identify pricing sensitivity and customer demand responses.
- Visualize trends by time and geography to understand seasonality and regional drivers.
- Provide data-driven recommendations for pricing, product mix, and distribution.

##  Dataset
- **Source**: Kaggle
- **Dataset Name**: Sample Superstore Food Sales Data
- **File**: `Sampledatafoodslaes.xlsx`

##  Key Analyses

### 1.  Exploratory Data Analysis (EDA)
- Checked for missing values, duplicates, and data types.
- Converted `OrderDate` to datetime and created new columns (`TotalSales`, `Month`, `Year`).
- Summary statistics and frequency analysis performed.
- Visualized quantity and price distributions using histograms and box plots.
- Correlation heatmap used to assess relationships between numerical features.
- Initial time-series visualizations highlighted monthly and yearly sales trends.

- <img width="596" height="471" alt="Screenshot 2025-07-31 094107" src="https://github.com/user-attachments/assets/ada324ec-980c-4262-bedf-a08ab8563357" />
Quantity Distribution (How Much People Buy)
This chart shows how many units people usually buy at a time.

Most customers buy between 20 and 60 items in a single order.

Very few people buy more than 100 items — that's rare.

 What this means: Most purchases are small to medium in size. Bulk buying is uncommon, so the business might be dealing with regular consumers or small stores, not wholesalers.

 <img width="596" height="471" alt="Screenshot 2025-07-31 094116" src="https://github.com/user-attachments/assets/97d1c614-14fb-4807-a33a-0e7a35b0396a" />
 2. Unit Price Distribution (How Much Items Cost)
This chart shows how prices are spread across products.

Most items are priced between $1.50 and $2.00.

Only a few products cost more than $2.50.

 What this means: The business mainly sells affordable products. There are a few higher-priced items, but most things fall into a low price range — ideal for frequent purchase

 <img width="598" height="471" alt="Screenshot 2025-07-31 094127" src="https://github.com/user-attachments/assets/8876e0d5-0947-43a7-b69e-4354ccc8e99f" />
 Quantity by Category (What Sells the Most)
This chart compares how many units are sold in each product category (like cookies, snacks, etc.).

Cookies are the top seller with the highest quantities sold.

Crackers and Snacks sell less and show smaller purchase amounts.

 What this means: Cookies are very popular. People buy a lot of them, possibly in bulk. The business should focus on cookies for promotions or combo offers

 <img width="595" height="473" alt="Screenshot 2025-07-31 094137" src="https://github.com/user-attachments/assets/e4b4f739-a1a1-4c4a-9722-545ade35b680" />
  Unit Price by Category (Which Products Cost More)
This chart shows how prices differ between product categories.

Crackers are priced higher and consistently so — they’re probably premium items.

Cookies have a wider price range — some are cheap, others more expensive.

 What this means: Crackers might be marketed as premium snacks, while cookies appeal to a wider audience with more variety.

 <img width="498" height="473" alt="Screenshot 2025-07-31 094151" src="https://github.com/user-attachments/assets/edf42f6b-400f-4cb5-a938-f3beb384183c" />
 5. Correlation Heatmap (How Numbers Are Connected)
This chart shows how different things relate to each other:

TotalSales and Quantity are strongly connected (when people buy more, total sales go up — no surprise!).

Price and Quantity have a slight negative connection — higher prices usually lead to fewer items sold.

 What this means: Customers are a bit sensitive to price. If you raise prices too much, they may buy fewer items. Keeping prices balanced could improve sales volume

 <img width="796" height="471" alt="Screenshot 2025-07-31 094200" src="https://github.com/user-attachments/assets/8e4b4507-4805-48bb-b795-ae7dd62b45a8" />
 Daily Sales Trend (How Sales Move Over Time)
This chart shows daily total sales across the time period.

Sales jump up and down frequently — some days are much busier than others.

There are clear spikes — likely special offers or high-demand periods.

 What this means: Sales are active and show some natural rhythm. Spikes can help plan future promotions — find out what caused them and repeat it.

 <img width="1002" height="571" alt="Screenshot 2025-07-31 094212" src="https://github.com/user-attachments/assets/a41bbf35-9002-45d5-9a52-38b4fef1ce4c" />
  Monthly Sales Comparison by Year
This chart compares monthly sales in 2020 vs. 2021.

Sales peak in June 2020 and November 2021.

2021 seems stronger in the second half of the year, especially toward the holidays.

 What this means: There’s a seasonal pattern. Sales go up around the middle and end of the year. This could be linked to school holidays, festive periods, or shopping events.

 







### 2. 🌍 Geographical Insights
- Compared total sales and quantity sold by **region**.
- Identified **top-performing cities** using revenue and volume analysis.
- Provided regional snapshots through side-by-side bar plots.

- <img width="1195" height="560" alt="Screenshot 2025-07-31 095141" src="https://github.com/user-attachments/assets/defa45ed-9509-4512-a947-4a500e274733" />
1. Total Sales by Region (Left chart in the image)
This bar chart compares total sales between two regions: East and West.

The East region shows significantly higher sales (over 21,000 units) compared to the West region (about 12,000 units).

This suggests that customers in the East are either buying more expensive products or purchasing in higher volumes.

From a business perspective, the East region is performing much better in terms of revenue and might be worth further investment or marketing support.

 Takeaway: The East region is a top-performing region in terms of revenue.

 2. Total Quantity by Region (Right chart in the image)
This chart shows the number of items sold in each region, regardless of price.

The East region again leads with around 9,700 units sold, while the West region trails with just under 6,000 units.

This reinforces the earlier sales chart, showing that the East region is not just selling expensive items, but selling more units overall.

 Takeaway: The East has both higher volume and value in sales, indicating stronger customer demand

 <img width="1187" height="561" alt="Screenshot 2025-07-31 095152" src="https://github.com/user-attachments/assets/07447249-db48-41c5-8cc5-8d37dd96ac65" />
  3. Total Sales by City (Left chart in the image)
This graph breaks total sales down by city.

Boston is the top city in terms of revenue, with sales crossing 13,000 units.

New York and Los Angeles are fairly close, with around 7,800–8,300 units.

San Diego shows the lowest performance, with just over 4,000 units.

 Takeaway: Boston is a standout city for revenue, while San Diego may need attention or a different sales strategy.

 4. Total Quantity by City (Right chart in the image)
This chart tracks the total number of items sold in each city.

Once again, Boston leads, selling about 5,600 items, confirming it’s not just selling expensive products, but selling a lot of products.

New York and Los Angeles are close behind, with similar quantities.

San Diego again ranks lowest with just around 2,000 items sold.

 Takeaway: Boston is the strongest city by both value and volume; San Diego has the lowest customer engagement.


### 3. 🗂️ Category-wise Analysis
- Summed total quantity sold and total revenue per product category.
- Used box plots to illustrate how unit prices differ across categories.
- Highlighted which categories drive volume and which are premium-priced.

- <img width="592" height="460" alt="Screenshot 2025-07-31 095640" src="https://github.com/user-attachments/assets/415bd259-2bf7-4573-a5cc-e4f266cc9470" />
Total Volume Sold by Category

This bar chart shows how many units were sold in each product category:

Cookies are the top-performing category by far, with the highest number of items sold.

Bars also performed well, selling slightly less than cookies.

Crackers and Snacks sold in much lower volumes, with crackers having the lowest total quantity sold.

 Interpretation: Cookies and bars are the most popular products by volume, suggesting strong customer preference or better distribution. The low sales of crackers and snacks might indicate weaker demand or less shelf visibility.

 <img width="582" height="454" alt="Screenshot 2025-07-31 095649" src="https://github.com/user-attachments/assets/3aae0503-3ce4-4703-9401-ed2484f01853" />
 Total Revenue by Category

This graph looks similar to the volume chart but focuses on total money earned rather than quantity sold.

Cookies again lead the pack, generating the highest revenue.

Bars follow closely, earning a solid amount of revenue.

Interestingly, Crackers earned more revenue than Snacks, despite both having low quantities sold.

 Interpretation: High unit prices could be helping products like crackers generate more money even if they sell fewer units. Cookies dominate in both volume and revenue — they’re both popular and profitable.

 <img width="792" height="561" alt="Screenshot 2025-07-31 095659" src="https://github.com/user-attachments/assets/ed80f34c-a8b3-42bc-90fd-8d639372f8de" />
 Unit Price Distribution by Category

This boxplot shows how the unit prices vary within each category:

Cookies have a wider price range, meaning some cookies are much more expensive than others. This could be due to premium or specialty items.

Crackers have a very high and consistent price — notice there's almost no variation. Most crackers sell at a fixed premium rate.

Bars and Snacks have lower and tighter price ranges, meaning they're more affordable and consistent in pricing.

🔍 Interpretation:

The wide range in cookie prices gives flexibility — appealing to both budget and premium customers.

Crackers are priced high, which might limit sales volume.

Bars and snacks are more price-stable and might be more attractive to price-sensitive customers.



### 4. 💸 Price Sensitivity
- Analyzed the relationship between **Unit Price** and **Quantity Sold**.
- Used scatter plots with category coloring to visualize demand elasticity.
- Computed the correlation coefficient to quantify overall price sensitivity.
- Compared price ranges across categories using box plots.

<img width="987" height="659" alt="Screenshot 2025-07-31 100120" src="https://github.com/user-attachments/assets/b700f831-d57b-40ba-91d8-b112d43594c2" />

 Chart: Price Sensitivity – Unit Price vs Quantity Sold
 What this chart shows:
This scatter plot compares how many units of each product were sold at different price points, separated by category. Each dot is a product, colored by its category (Bars, Cookies, Crackers, or Snacks).

 Simple interpretation:
Most of the dots are grouped on the left side, where prices are lower (between $1.5 and $2.5).

This tells us that products priced lower tend to sell more units. That’s basic price sensitivity: when the price is low, people buy more.

Cookies (green dots) have a wide range of price points and are still bought a lot—even when the price goes up a bit. This might suggest that customers really like cookies and are less sensitive to their price.

Crackers (orange dots), on the other hand, are mostly at the highest price level ($3.5) and don’t sell nearly as much. So they’re more sensitive to price—people buy less when it costs more.

 What this means:
If you're pricing products, aim to stay in the lower range (below $2.5) for better sales volume—unless you're selling cookies, which people seem to buy even when prices go up.

<img width="1191" height="633" alt="Screenshot 2025-07-31 100130" src="https://github.com/user-attachments/assets/e453c73f-d3f6-49e1-8620-8f7cbcecdf51" />

Chart: Category-specific Unit Price Distribution
 What this chart shows:
This boxplot breaks down the price range for each category—showing how high or low the prices typically are, and how spread out they are.

 Simple interpretation:
Crackers have the highest and most fixed price—around $3.5—and the box is very small, which means almost all of them cost the same.

Cookies show the widest price range, with prices between about $1.8 to $2.8. That big box means a lot of variation.

Bars and Snacks both sit in the lower price range (around $1.7 to $2.0). These are more consistent and cheaper options.

 What this means:
If you want a budget-friendly category to promote, go for Bars or Snacks.

Crackers might be overpriced—they cost the most and don’t sell as much.

Cookies offer pricing flexibility. You can price them higher or lower and still sell well, because customers seem more willing to pay for them.


### 5. 📦 Product Mix & Contribution
- Calculated each product category’s contribution to overall revenue.
- Conducted a **Pareto Analysis (80/20 Rule)** to identify the top products driving the majority of revenue.
- Visualized both category-level and product-level contributions using bar charts and cumulative plots.

  <img width="992" height="563" alt="Screenshot 2025-07-31 100426" src="https://github.com/user-attachments/assets/ffe49657-3e89-40d8-a3c5-5aac1e47dbe9" />
 First Image: Category Contribution to Total Sales

What it shows:
This bar chart breaks down how much each product category (like Cookies, Bars, Crackers, and Snacks) contributed to the overall sales.

Layman explanation:

Think of this like a pie being shared among four groups.

Cookies got the biggest slice — they brought in the most sales, meaning they are the top-performing category.

Bars came next, performing quite well too.

Crackers and Snacks are far behind — these categories didn’t sell as much.

Why it matters:
This tells us where most of the money is coming from. If you're a business owner or store manager, you'd probably want to focus on promoting Cookies and Bars more, or figure out how to boost sales in Crackers and Snacks.

<img width="1184" height="619" alt="Screenshot 2025-07-31 100436" src="https://github.com/user-attachments/assets/c275022b-4eb0-4e84-a635-315af58ecd8d" />
Second Image: Pareto Analysis – Product Contribution to Sales

What it shows:
This is a Pareto chart, which helps us spot the products that are bringing in the most revenue — following the famous 80/20 rule (i.e., 80% of the results often come from just 20% of the inputs).

Layman explanation:

The blue bars show sales from individual products like Carrot, Oatmeal Raisin, Arrowroot, etc.

The red line tracks the cumulative contribution — how much each product adds up to the total.

The dashed horizontal line at 80% shows where the “magic” 80% of total sales lies.

What we learn from it:

Just 3–4 top products (like Carrot, Oatmeal Raisin, Arrowroot) are responsible for the majority of total sales.

Products beyond this point (like Pretzels, Banana) are contributing less.

Why it matters:
This helps in making smart decisions:

Focus your inventory, marketing, or pricing strategies on these top performers.

Consider whether to improve, repackage, or even phase out low performers.


### 6. 📈 Time Series Trends
- Evaluated **monthly** and **weekly** sales performance over time.
- Visualized **year-over-year seasonality** to identify consistent high and low periods.
- Seasonal insights help inform promotions and inventory planning.

- <img width="990" height="420" alt="Screenshot 2025-07-31 100753" src="https://github.com/user-attachments/assets/a6c8b2dd-6623-4e8a-87dc-e4d2baa616f2" />
   Monthly Sales Trend
What it shows:
A line plot of total sales per month across the dataset period (2020–2021).

Interpretation:

Sales are inconsistent month-to-month, with spikes in months like June 2020 and October 2021.

There’s no smooth upward or downward trend, suggesting external events or promotions might be influencing sales at certain times.

Business insight:
Identify and understand what caused high-performing months (e.g., promotions, product launches, holidays) to replicate their success.

<img width="1190" height="460" alt="Screenshot 2025-07-31 100803" src="https://github.com/user-attachments/assets/6acefc72-00dd-41e9-b971-52aa71f61902" />
Weekly Sales Trend
What it shows:
A finer-grained week-over-week view of total sales, useful for detecting short-term fluctuations.

Interpretation:

Weekly data is highly volatile, with several sharp peaks and drops.

The highest weekly sales occurred in late December 2020.

There's no strong consistent growth trend, but patterns might emerge with smoothing techniques.

Business insight:
You may benefit from weekly campaign planning or managing perishable inventory based on peak activity.

<img width="979" height="514" alt="Screenshot 2025-07-31 100814" src="https://github.com/user-attachments/assets/4f8c6d55-c1c5-474a-9bd7-b87153326bfb" />
Seasonality: Monthly Sales by Year

What it shows:
This chart compares monthly sales across two years (2020 and 2021) to detect seasonal patterns.

Interpretation:

In 2020, sales peaked in June and October.

In 2021, peak months shifted to November and December.

While both years share some consistent dips (like February and July), seasonality patterns vary year to year.

Business insight:
Understanding these seasonal shifts helps in forecasting demand and planning inventory or promotions. For instance, Q4 seems consistently strong in both years.




### 7. 🥇 Top & Bottom Performers
- Identified top and bottom 5 products by **quantity sold** and by **total revenue**.
- Helpful in identifying products that require push or should be phased out.
- Visualization includes bar charts sorted by performance metric.

- <img width="790" height="427" alt="Screenshot 2025-07-31 101212" src="https://github.com/user-attachments/assets/ca8d877a-36a3-475c-ab05-c4de276a513e" />
 Top 5 Products by Quantity Sold

This bar chart shows the five products that customers bought the most.

Carrot is the clear favorite. People bought it more than any other item—over 4,000 units!

Next is Oatmeal Raisin, followed by Arrowroot and Chocolate Chip cookies.

Interestingly, Bran is also on this list, meaning it’s fairly popular too.

 What this means: These are the most in-demand products. If you're a store owner, you’d want to always keep these stocked and maybe even promote them more because people are buying them often.

 <img width="798" height="460" alt="Screenshot 2025-07-31 101226" src="https://github.com/user-attachments/assets/d799298a-6b48-4b13-9bbc-ce14272bef8d" />
  Bottom 5 Products by Quantity Sold

This one shows the least purchased products.

Banana was the lowest seller—almost no one bought it.

Pretzels also had very few sales.

Whole Wheat, Potato Chips, and surprisingly, Bran show up here too (probably a different version or size than the one in the top list).

 What this means: These products aren’t moving off the shelves. They might not be appealing, could be overpriced, or just not promoted well. It might be time to rethink how they’re marketed—or even consider removing them.

 <img width="790" height="459" alt="Screenshot 2025-07-31 101234" src="https://github.com/user-attachments/assets/87832fed-42a1-46e6-822c-1a36a561ce62" />
 Top 5 Products by Total Revenue

Here, we’re not looking at how many items were sold—but how much money each product made overall.

Carrot tops the chart again. Not only is it popular, it brings in the most cash.

Oatmeal Raisin and Arrowroot also make a lot of money.

Even though Chocolate Chip and Whole Wheat didn’t top the quantity chart, they still brought in good money—maybe because they are priced higher.

 What this means: These are the products that make the most money, not just the most sales. This is useful for deciding what products to feature if your goal is to increase revenue.

 <img width="787" height="462" alt="Screenshot 2025-07-31 101243" src="https://github.com/user-attachments/assets/b5fe05d3-f5c6-4f7c-9f90-4df0d7d4a20b" />
 Bottom 5 Products by Total Revenue

This graph shows the products that brought in the least amount of money.

Banana made the least. It sold poorly and it’s probably cheap, which explains the low revenue.

Pretzels, Potato Chips, and Bran are here again, showing weak performance.

Whole Wheat, which appeared in both top and bottom lists, probably has different versions (some doing well, others not so much).

 What this means: These items didn’t earn much money. This could be due to low prices, low demand, or both. If you're managing a shop, you'd want to investigate: Are these products worth keeping? Can pricing or promotions help?

  Summary (in plain terms):
Carrot is the superstar: lots of people buy it and it makes the most money.

Banana and Pretzels are doing the worst in both sales and revenue.

Bran and Whole Wheat show up in both top and bottom lists, which suggests there are probably different sizes or types of these products being sold.





### 8. 🧩 Performance Analysis by Dimensions
- Deep-dived into product, city, and category level performance.
- Summarized top 5 cities and products by revenue.
- Displayed clear views of product and region combinations that drive business.

  <img width="586" height="457" alt="Screenshot 2025-07-31 101909" src="https://github.com/user-attachments/assets/98d361a5-73e3-44f3-b035-5bfa167495c3" />
  Total Sales by Region
This chart shows us how much was sold in two different regions: East and West.

You can see the East region did way better — it brought in over 20,000 units in sales, while the West only made about 12,000.

That’s a big difference, and it tells us that the East is clearly the stronger performer.

Maybe they have more stores, better marketing, or just more customers — either way, it’s worth digging into why the East is doing so well.

<img width="782" height="464" alt="Screenshot 2025-07-31 101917" src="https://github.com/user-attachments/assets/8ad1a676-2a5a-4deb-9b58-57266ca0201e" />
 2. Top 5 Cities by Total Sales
Here we’re looking at which cities brought in the most sales.

Boston is way ahead of the others — with total sales over 13,000.

Then we have New York, Los Angeles, and San Diego following behind.

What’s missing here is the fifth city — it looks like the chart cut off the last one (a small fix needed).

Still, the takeaway is clear: these cities are hotspots for sales and should probably get more focus — more inventory, more promos, maybe even more stores.

<img width="789" height="422" alt="Screenshot 2025-07-31 101926" src="https://github.com/user-attachments/assets/5280d6e2-19b3-4b70-b524-2aaf7feb8bd3" />
 Top 5 Products by Total Sales
This one shows the five best-selling products.

Carrot and Oatmeal Raisin products are clearly customer favorites — both selling over 7,000 units.

Products like Arrowroot, Chocolate Chip, and Whole Wheat also did well but not as much.

This kind of insight helps a lot: if you're running the business, you’d want to keep these top sellers in stock and maybe even promote them more.

<img width="583" height="425" alt="Screenshot 2025-07-31 101936" src="https://github.com/user-attachments/assets/dd43b6b5-8956-4e03-8c3e-564cd9a5e597" />
 Total Sales by Category
This chart breaks sales down by type of product.

Cookies are the winners by a long shot — with around 17,000 in sales.

Bars come next with about 10,000, but after that, sales drop off.

Crackers and Snacks made very little by comparison.

This tells us where the money is coming from: Cookies and Bars are the breadwinners, so focus should probably stay there unless the other categories get some help.

<img width="983" height="520" alt="Screenshot 2025-07-31 101947" src="https://github.com/user-attachments/assets/f3a08518-517e-4c35-832f-0531afe9941e" />
Monthly Sales by Year
This one’s a bit more detailed — it shows how sales changed month by month, comparing 2020 (light bars) and 2021 (dark bars).

You can spot some trends: for example, June 2020 had a huge spike, while November 2021 also saw a major jump.

This kind of pattern could mean people buy more in the summer and just before the holidays.

It also shows how some months are consistently better than others — like October through December.

Knowing this helps with planning ahead — like when to run big promos or when to expect slower periods

In Summary:
These graphs give you a full picture of:

Where your sales are coming from (East region, cities like Boston),

What people are buying (Carrot products, Cookies),

When they’re buying (summer and holiday months),

And which areas need more attention (West region, low-performing product categories).






  Project Summary:
This project has been a deep, eye-opening journey for me into the world of customer buying behavior and product performance in food retail. I wanted to go beyond surface-level numbers and truly understand:
 What are people actually buying?
 Where are they buying it?
 When do they buy more?
 And how does pricing affect their choices?

 Why I Took On This Project
I’ve always been curious about the decisions customers make—especially when faced with variety and price tags. Using real data from a Kaggle dataset, I wanted to see what insights I could uncover that would help any food business make smarter decisions.

So I rolled up my sleeves, cleaned the data, ran the numbers, and visualized the story hidden in the spreadsheet.

 What I Discovered
 Geography Really Matters
The East region clearly outperformed the West in both sales volume and revenue.

Boston stood out as a sales powerhouse—it consistently brought in the highest numbers. It made me think: what is Boston doing right? Better marketing, higher demand, or simply better distribution?

 Some Products Just Click
Cookies ruled the market—especially Carrot and Oatmeal Raisin. People love them and they’re buying them in bulk.

Meanwhile, Crackers and Snacks didn’t make much of a splash. They're slow movers, and probably not worth stocking up on heavily unless things change.

Timing Is Everything
June and November were hot sales months—possibly tied to summer activity and early holiday shopping.

July and September slowed down—maybe due to vacations or back-to-school budgeting. Knowing this helps with stock planning and promotions.

 Pricing Isn't One-Size-Fits-All
Overall, there's a trend: when prices go up, quantity drops.

But there were exceptions. Some products still sold well even at higher prices, which signals strong brand loyalty or product uniqueness.

 What This Means (From My Point of View)
After exploring all this, a few things became crystal clear:

Location and category matter a lot—more than we sometimes realize.

Timing can make or break monthly sales, and that should guide marketing calendars.

Not all customers are price-sensitive. For certain products, you can hold your price and still win.

 Personal Takeaway
Doing this project helped me see how data can directly inform smart business decisions—whether it’s what to stock, when to run a promo, or how to set prices.
It also gave me hands-on experience in real-world EDA (Exploratory Data Analysis) and storytelling through data.

This wasn’t just about charts and graphs—it was about listening to what the customers are “saying” through their actions.

 Technologies Used
Python
Utilized as the primary programming language for data analysis and modeling.

Pandas
For data cleaning, manipulation, and aggregation.

Seaborn & Matplotlib
Used for data visualization to uncover patterns, trends, and insights in the dataset.

Scikit-learn (Sklearn)

Machine Learning:

Random Forest: For classification and feature importance analysis.

KMeans: For customer or product segmentation through clustering.

Dimensionality Reduction:

PCA (Principal Component Analysis): Used to reduce complexity and visualize high-dimensional data.


##  Recommendations
- **Focus on High Performers**: Invest in marketing and supply chain support for top products contributing to the majority of sales.
- **Manage Low Performers**: Reassess or phase out products with consistently low quantity and revenue.
- **Dynamic Pricing**: Use price sensitivity findings to guide discount strategies, especially in price-elastic categories.
- **Leverage Seasonality**: Align promotions and inventory buildup with months that show strong historical sales.
- **Optimize by Region**: Adjust product availability based on what sells best in each region or city.
- **Monitor Trends**: Establish ongoing dashboards to track performance metrics, trends, and price-response regularly.

   Running the Code
To replicate and interact with this analysis on your own machine, follow these steps:

Set Up Environment
Ensure you have Python installed along with the following key libraries:
pandas, seaborn, matplotlib, scikit-learn, openpyxl, and prophet (if time series forecasting is included).

Open the Notebook or Script
Clone this repository or simply open the .ipynb Jupyter Notebook in your preferred Python IDE (like VS Code, JupyterLab, or Anaconda).

Load the Dataset
Ensure the Excel file Sampledatafoodsales.xlsx is in the same directory as your notebook.

Run Analysis Sections
Execute the notebook step by step, organized in the following flow:

1. Exploratory Data Analysis (EDA)
Initial investigation to understand data distribution, detect missing values, and shape the overall structure.

2. Visualizations
Graphical insights such as product performance, category-wise contributions, price sensitivity, time series patterns, and geographic sales spread.

3. Business Insights
Interpret visual findings to reveal customer preferences, top and bottom performers, pricing effects, and category strengths.

Project Status
Complete — Models and insights validated. Ready for presentation, reporting, or deployment.

Author
Damilare Igbosanya

License
This project is released for educational and portfolio purposes.

---
_This project is a step toward smarter, more data-driven retail management that aligns with both customer demand and business priorities._
