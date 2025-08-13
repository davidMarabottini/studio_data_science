import matplotlib.pyplot as plt

def print_features_bar(X, feature, y, type='numerical', grouping=5):
    fig, ax = plt.subplots(figsize=(12, 4))
    
    temp = X.copy()
    temp['y'] = y
    
    if type == 'numerical':
        temp['bin'] = (temp[feature] // grouping) * grouping
    else:
        temp['bin'] = temp[feature]
    
    grouped = temp.groupby('bin').agg(
        count = ('y', 'size'),
        perc_y1 = ('y', lambda x: 100 * (x.sum() / len(x)))
    ).sort_index()
    
    cmap = plt.cm.Reds
    normed = grouped['perc_y1'] / grouped['perc_y1'].max()
    colors = cmap(normed)
    
    bars = ax.bar(range(len(grouped)), grouped['count'], color=colors)
    
    ax.set_title(f'Feature: {feature}')
    ax.set_xlabel(feature)
    ax.set_ylabel('Count')
    
    labels = [
        f"{label} ({count}; {perc:.0f}%)" 
        for label, count, perc in zip(grouped.index, grouped['count'], grouped['perc_y1'])
    ]
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=90)
    
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(0, grouped['perc_y1'].max()))
    sm.set_array([])
    cbar = fig.colorbar(sm, ax=ax)
    cbar.set_label('% di sopravvissuti sul titanic (y=1)')
    
    plt.show()