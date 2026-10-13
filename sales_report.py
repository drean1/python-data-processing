import polars as pl

#question no.3
df = pl.read_csv("sales.csv") #untuk load/ambil data dari sales.csv
#print(df)

#question no.4 
filtered_df = df.filter(  #digunakan untuk menyaring baris berdasarkan kondisi tertentu.
   pl.col("region") == "East", 
)
#print(filtered_df)

#question no.5
grouped_df = (      #untuk kelompokan data berdasarkan jenis kolom pada kolom yang diambil
    filtered_df.group_by("product")
    .agg(pl.col("sales").sum()) #menjumlahkan total angka pada kolom yang dipilih 
    .sort("sales", descending=True)  #mengurutkan hasil dari angka terbesar ke terkecil
)
#print(grouped_df)

#question no.6
df_sales = pl.read_csv("sales.csv") #load/ambil data dari sales.csv
df_product = pl.read_csv("product_info.csv") #load/ambil data dari product_info.csv

joined_df = df_sales.join(df_product, on="product", how="left") #untuk menggabungkan kedua dataframe menggunakan metode left join berdsarkan kolom 

#print(joined_df)

#question no.7
df_pivot = joined_df.pivot( #untuk mengubah table yang di inginkan 
    index="region",
    on="product",
    values="sales",
    aggregate_function="sum"
)

df_pivot = df_pivot.select(     #untuk memilih/mengatur ulang urutan kolom yang ingin ditampilkan secara spesifik
    ["region", "Gadget", "Widget"]
)

#print(df_pivot)

#question no.8
df_manager = pl.read_csv("manager.csv") #load/mengambil data dari manager.csv

# Menggabungkan dataframe hasil dari soal sebelumnya (joined_df) dengan df_manager menggunakan Left Join
# Penggabungan kali ini dilakukan berdasarkan kolom "region" sebagai kunci penghubungnya
final_joined_df = joined_df.join(df_manager, on="region", how="left") 

#print(final_joined_df)