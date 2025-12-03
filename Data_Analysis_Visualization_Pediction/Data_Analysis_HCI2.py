# import pandas as pd
# import matplotlib.pyplot as plt
#
# # Load the dataset (using the fixed filename and correct column names)
# df = pd.read_csv('titian_palladio_ready_fixed.csv')
#
# print("Dataset columns:", df.columns.tolist())
# print("Dataset shape:", df.shape)
# print("\nFirst few rows:")
# print(df.head())
#
# # Data preparation for 5 questions
# # Q1: Titian genres 1530-1540
# q1_data = df[(df['Year Created'] >= 1530) & (df['Year Created'] <= 1540)]['Artwork Genre'].value_counts()
#
# # Q2: Philip II artworks by genre
# q2_data = df[df['Patron'].str.contains('Philip II', na=False)]['Artwork Genre'].value_counts()
#
# # Q3: Venice-based patrons supporting religious artworks
# q3_data = df[(df['Patron Origin place'] == 'Venice') & (df['Artwork Genre'] == 'religious')]['Patron'].value_counts().head(10)
#
# # Private patrons outside Venice, myth artworks 1540-1570
# # Step-by-step filtering to avoid boolean indexing issues
# year_mask = (df['Year Created'] >= 1540) & (df['Year Created'] <= 1570)
# private_mask = df['Patron Type'] == 'private'
# myth_mask = df['Artwork Genre'] == 'myth'
# not_venice_mask = df['Patron Origin place'] != 'Venice'
#
# # Combine conditions safely
# q4_mask = year_mask & private_mask & myth_mask & not_venice_mask
# q4_data = df[q4_mask]['Patron'].value_counts().head(8)
#
# # Q5: Unknown patrons by origin distance from Venice (simplified by unique origins)
# q5_data = df[(df['Patron'] == 'unknown') & (df['Place Created'] == 'Venice')]['Patron Origin place'].value_counts()
#
# # Create comprehensive visualization
# fig, axes = plt.subplots(3, 2, figsize=(20, 18))
# fig.suptitle('Titian Artworks Analysis - 5 Key Questions', fontsize=20, y=0.98)
#
# # Q1
# axes[0,0].bar(range(len(q1_data)), q1_data.values, color='skyblue')
# axes[0,0].set_title('Q1: Titian Genres (1530-1540)', fontsize=14, fontweight='bold')
# axes[0,0].set_xticks(range(len(q1_data)))
# axes[0,0].set_xticklabels(q1_data.index, rotation=45, ha='right')
# axes[0,0].set_ylabel('Number of Artworks')
#
# # Q2
# axes[0,1].bar(range(len(q2_data)), q2_data.values, color='coral')
# axes[0,1].set_title('Q2: Philip II Supported Genres', fontsize=14, fontweight='bold')
# axes[0,1].set_xticks(range(len(q2_data)))
# axes[0,1].set_xticklabels(q2_data.index, rotation=45, ha='right')
# axes[0,1].set_ylabel('Number of Artworks')
#
# # Q3
# axes[1,0].bar(range(len(q3_data)), q3_data.values, color='lightgreen')
# axes[1,0].set_title('Q3: Top Venice Patrons - Religious Art', fontsize=14, fontweight='bold')
# axes[1,0].set_xticks(range(len(q3_data)))
# axes[1,0].set_xticklabels(q3_data.index, rotation=45, ha='right')
# axes[1,0].set_ylabel('Number of Artworks')
#
# # Q4
# axes[1,1].bar(range(len(q4_data)), q4_data.values, color='gold')
# axes[1,1].set_title('Q4: Private Patrons Outside Venice - Myth (1540-1570)', fontsize=14, fontweight='bold')
# axes[1,1].set_xticks(range(len(q4_data)))
# axes[1,1].set_xticklabels(q4_data.index, rotation=45, ha='right')
# axes[1,1].set_ylabel('Number of Artworks')
#
# # Q5
# axes[2,0].bar(range(len(q5_data)), q5_data.values, color='plum')
# axes[2,0].set_title('Q5: Unknown Patrons for Venice Artworks', fontsize=14, fontweight='bold')
# axes[2,0].set_xticks(range(len(q5_data)))
# axes[2,0].set_xticklabels(q5_data.index, rotation=45, ha='right')
# axes[2,0].set_ylabel('Number of Artworks')
#
# # Hide the empty subplot
# axes[2,1].set_visible(False)
#
# plt.tight_layout()
# plt.savefig('titian_analysis_5_questions.png', dpi=300, bbox_inches='tight')
# plt.show()
#
# # Print summary statistics
# print("\n=== SUMMARY STATISTICS ===")
# print(f"Q1 - Top genre 1530-1540: {q1_data.index[0]} ({q1_data.iloc[0]} artworks)")
# print(f"Q2 - Philip II top genre: {q2_data.index[0]} ({q2_data.iloc[0]} artworks)")
# print(f"Q3 - Top Venice religious patron: {q3_data.index[0]} ({q3_data.iloc[0]} artworks)")
# print(f"Q4 - Top private myth patron (1540-1570): {q4_data.index[0]} ({q4_data.iloc[0]} artworks)")
# print(f"Q5 - Most frequent unknown patron origin: {q5_data.index[0]} ({q5_data.iloc[0]} artworks)")
# print(f"\nTotal artworks analyzed: {len(df)}")


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_titian_visualizations():
    # 1. Load the dataset
    try:
        df = pd.read_csv('titian_palladio_ready_fixed.csv')
    except FileNotFoundError:
        print("Error: 'titian_palladio_ready_fixed.csv' not found. Please ensure the file is in the same directory.")
        return

    # Set the visual style
    sns.set_theme(style="whitegrid")

    # Create a figure with a grid layout for the 5 questions
    # Layout: 3 rows, 2 columns (last slot can be empty or used for text)
    fig, axes = plt.subplots(3, 2, figsize=(18, 18))
    fig.suptitle('Titian Data Analysis Dashboard', fontsize=24, weight='bold', y=0.95)

    # ---------------------------------------------------------
    # Q1: Genre Focus (1530-1540)
    # ---------------------------------------------------------
    q1_df = df[(df['Year Created'] >= 1530) & (df['Year Created'] <= 1540)]
    q1_counts = q1_df['Artwork Genre'].value_counts().reset_index()
    q1_counts.columns = ['Genre', 'Count']

    sns.barplot(data=q1_counts, x='Genre', y='Count', ax=axes[0, 0], palette='viridis')
    axes[0, 0].set_title('Q1: Artwork Genres (1530-1540)', fontsize=16)
    axes[0, 0].set_ylabel('Number of Artworks')
    axes[0, 0].bar_label(axes[0, 0].containers[0])

    # ---------------------------------------------------------
    # Q2: Philip II Support
    # ---------------------------------------------------------
    # Filter for Philip II (handling variations if necessary, but 'Philip II' is standard in this dataset)
    q2_df = df[df['Patron'] == 'Philip II']
    q2_counts = q2_df['Artwork Genre'].value_counts().reset_index()
    q2_counts.columns = ['Genre', 'Count']

    sns.barplot(data=q2_counts, x='Genre', y='Count', ax=axes[0, 1], palette='magma')
    axes[0, 1].set_title('Q2: Genres Supported by Philip II', fontsize=16)
    axes[0, 1].set_ylabel('Number of Artworks')
    axes[0, 1].bar_label(axes[0, 1].containers[0])
    # Add text annotation for location
    axes[0, 1].text(0.5, 0.9, "All created in Venice", transform=axes[0, 1].transAxes,
                    ha='center', fontsize=12, bbox=dict(facecolor='white', alpha=0.8))

    # ---------------------------------------------------------
    # Q3: Venetian Patrons & Religion
    # ---------------------------------------------------------
    q3_df = df[(df['Patron Origin place'] == 'Venice') & (df['Artwork Genre'] == 'religious')]
    q3_counts = q3_df['Patron'].value_counts().head(7).reset_index() # Top 7 for clarity
    q3_counts.columns = ['Patron', 'Count']

    sns.barplot(data=q3_counts, y='Patron', x='Count', ax=axes[1, 0], palette='Blues_r')
    axes[1, 0].set_title('Q3: Top Venetian Patrons (Religious Art)', fontsize=16)
    axes[1, 0].set_xlabel('Number of Artworks')
    axes[1, 0].bar_label(axes[1, 0].containers[0])

    # ---------------------------------------------------------
    # Q4: Private Patrons Outside Venice (Myth, 1540-1570)
    # ---------------------------------------------------------
    q4_df = df[
        (df['Patron Type'] == 'private') &
        (df['Patron Origin place'] != 'Venice') &
        (df['Year Created'] >= 1540) &
        (df['Year Created'] <= 1570) &
        (df['Artwork Genre'] == 'myth')
        ]
    q4_counts = q4_df['Patron'].value_counts().reset_index()
    q4_counts.columns = ['Patron', 'Count']

    if not q4_counts.empty:
        sns.barplot(data=q4_counts, y='Patron', x='Count', ax=axes[1, 1], palette='Reds_r')
        axes[1, 1].set_title('Q4: Private Non-Venetian Patrons (Myth, 1540-1570)', fontsize=16)
        axes[1, 1].set_xlabel('Number of Artworks')
        axes[1, 1].set_xticks(range(0, max(q4_counts['Count'])+2)) # Integer ticks
    else:
        axes[1, 1].text(0.5, 0.5, "No data found for criteria", ha='center')

    # ---------------------------------------------------------
    # Q5: Distance of Unknown Patrons (Artworks created in Venice)
    # ---------------------------------------------------------
    # Logic: Identify unknown patrons, find their origin, and map approx distance to Venice
    q5_df = df[
        (df['Patron'].str.lower() == 'unknown') &
        (df['Place Created'] == 'Venice')
        ]
    origins = q5_df['Patron Origin place'].unique()

    # Hardcoded approximate distances from Venice (in km) for visualization
    # Derived from geographical knowledge
    distances = {
        'Venice': 0,
        'Padua': 40,
        'Ferrara': 110,
        'Urbino': 250
    }

    # Filter distances to only include origins present in the data
    plot_data = [{'City': city, 'Distance (km)': distances.get(city, 0)} for city in origins if city in distances]
    q5_plot_df = pd.DataFrame(plot_data).sort_values('Distance (km)', ascending=False)

    sns.barplot(data=q5_plot_df, x='City', y='Distance (km)', ax=axes[2, 0], palette='cool')
    axes[2, 0].set_title('Q5: Distance of "Unknown" Patrons from Venice', fontsize=16)
    axes[2, 0].set_ylabel('Approximate Distance (km)')
    axes[2, 0].bar_label(axes[2, 0].containers[0])

    # ---------------------------------------------------------
    # Final Cleanup (Remove empty subplot if odd number)
    # ---------------------------------------------------------
    axes[2, 1].axis('off') # Turn off the 6th subplot frame

    # Add a summary text in the empty slot
    summary_text = (
        "SUMMARY OF FINDINGS\n\n"
        "1. Focus (1530-1540): Portraiture was the dominant genre.\n\n"
        "2. Philip II: Heavily supported Religious art; all created in Venice.\n\n"
        "3. Venetian Religion: The Ducal Palace was the top local patron.\n\n"
        "4. Myth (1540-1570): Alfonso d'Avalos & Cardinal Farnese\n"
        "   were key private patrons outside Venice.\n\n"
        "5. Most Distant Unknown: A patron from Urbino (~250km away)."
    )
    axes[2, 1].text(0.1, 0.5, summary_text, fontsize=14, va='center', ha='left', family='monospace')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # Adjust for suptitle

    # Save and Show
    output_filename = 'titian_analysis_dashboard.png'
    plt.savefig(output_filename)
    print(f"Dashboard saved as '{output_filename}'")
    plt.show()

if __name__ == "__main__":
    generate_titian_visualizations()
