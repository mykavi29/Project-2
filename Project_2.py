{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "62969be2-76c1-4146-98ab-3361788e974a",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-12-30 21:58:53.570 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run /opt/anaconda3/lib/python3.12/site-packages/ipykernel_launcher.py [ARGUMENTS]\n",
      "2024-12-30 21:58:53.571 Session state does not function when running a script without `streamlit run`\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import streamlit as st\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "# Step 1: Calculate Key Metrics\n",
    "def calculate_cre_metrics(price, noi, down_payment, financing_cost):\n",
    "    cap_rate = (noi / price) * 100  # Capitalization Rate\n",
    "    cash_on_cash_return = ((noi - financing_cost) / down_payment) * 100  # Cash-on-Cash Return\n",
    "    return cap_rate, cash_on_cash_return\n",
    "\n",
    "# Step 2: Collect Property Data\n",
    "def collect_property_data():\n",
    "    st.title(\"Commercial Real Estate Analysis Tool\")\n",
    "    st.sidebar.header(\"Enter Property Details\")\n",
    "\n",
    "    num_properties = st.sidebar.number_input(\"Number of Properties\", min_value=1, value=3)\n",
    "\n",
    "    properties = []\n",
    "    for i in range(num_properties):\n",
    "        st.sidebar.subheader(f\"Property {i + 1}\")\n",
    "        price = st.sidebar.number_input(f\"Purchase Price of Property {i + 1} ($)\", min_value=1)\n",
    "        noi = st.sidebar.number_input(f\"Annual NOI for Property {i + 1} ($)\", min_value=1)\n",
    "        down_payment = st.sidebar.number_input(f\"Down Payment for Property {i + 1} ($)\", min_value=1)\n",
    "        financing_cost = st.sidebar.number_input(f\"Annual Financing Cost for Property {i + 1} ($)\", min_value=0)\n",
    "        properties.append({\"Price\": price, \"NOI\": noi, \"Down Payment\": down_payment, \"Financing Cost\": financing_cost})\n",
    "    \n",
    "    return pd.DataFrame(properties)\n",
    "\n",
    "# Step 3: Visualization\n",
    "def visualize_metrics(properties):\n",
    "    properties['Cap Rate'], properties['Cash-on-Cash Return'] = zip(\n",
    "        *properties.apply(lambda row: calculate_cre_metrics(\n",
    "            row['Price'], row['NOI'], row['Down Payment'], row['Financing Cost']), axis=1)\n",
    "    )\n",
    "\n",
    "    # Display the data\n",
    "    st.write(\"### Property Data with Metrics\")\n",
    "    st.dataframe(properties)\n",
    "\n",
    "    # Bar Chart for Cap Rate and Cash-on-Cash Return\n",
    "    st.write(\"### Cap Rate vs. Cash-on-Cash Return\")\n",
    "    fig, ax = plt.subplots(figsize=(10, 6))\n",
    "    properties[['Cap Rate', 'Cash-on-Cash Return']].plot(kind='bar', ax=ax, color=['skyblue', 'orange'])\n",
    "    ax.set_xticks(range(len(properties)))\n",
    "    ax.set_xticklabels([f\"Property {i+1}\" for i in range(len(properties))])\n",
    "    ax.set_title(\"Cap Rate vs. Cash-on-Cash Return\")\n",
    "    ax.set_ylabel(\"Percentage (%)\")\n",
    "    plt.grid(axis='y')\n",
    "    st.pyplot(fig)\n",
    "\n",
    "    # Insights\n",
    "    best_property = properties.loc[properties['Cash-on-Cash Return'].idxmax()]\n",
    "    st.success(f\"🏆 Best Property: Property {properties.index.get_loc(best_property.name) + 1} with a Cash-on-Cash Return of {best_property['Cash-on-Cash Return']:.2f}%\")\n",
    "\n",
    "# Step 4: Main Function\n",
    "def main():\n",
    "    properties = collect_property_data()\n",
    "    if not properties.empty:\n",
    "        visualize_metrics(properties)\n",
    "\n",
    "# Step 5: Run the App\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
