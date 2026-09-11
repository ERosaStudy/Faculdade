import numpy as np

dataset =np.loadtxt ('social_media.csv', delimiter=';',dtype=str, encoding='utf-8')
header = dataset[0]
body = dataset[1:]

##exercicio 1 

content_count = np.sum(dataset[:, 3] == "Video")
print(f'EXERCICIO 1: Quantidade de posts de vídeo:{content_count}')
print('')

##Exercicio 2 

low_engagement_count = np.sum(dataset[:, 9] == "Low")
post_total = len(body)
porcentagem = (low_engagement_count / post_total) * 100

print (f"EXERCICIO 2: Porcentagem de posts de baixo engajamento: {porcentagem:.2f}%")
print('')

##Exercicio 3

tiktok_filter = dataset[:,1] == "TikTok"
shares_sum = np.sum(dataset[tiktok_filter, 7].astype(int))
comment_sum = np.sum(dataset[tiktok_filter,8].astype(int))

dicionario = {"Compartilhamentos": int(shares_sum), "Comentários": int(comment_sum)}
print(f"EXERCICIO 3: {dicionario}")
print('')

##exercicio 4

region_filter = dataset[:,4]
region_counts = np.unique(region_filter, return_counts=True)
max_region_index = np.argmax(region_counts[1])
max_region_name = region_counts[0][max_region_index]
max_region_count = region_counts[1][max_region_index]

print(f"EXERCICIO 4: Região com maior quantidade de posts: {max_region_name} ({max_region_count} posts)")
print('')

##exercicio 5

views = body[:, 5].astype(int)
max_views_index = np.argmax(views)
max_views_value = views[max_views_index]
max_view_platform = body[max_views_index, 1]

print(f"EXERCICIO 5: Plataforma: {max_view_platform} | Views: {max_views_value}")



