import pandas as pd
import os

def load_data(file_path):
    """Fungsi untuk memuat dataset raw."""
    print(f"Memuat data dari {file_path}...")
    return pd.read_csv(file_path)

def preprocess_data(df):
    """Fungsi untuk melakukan tahapan preprocessing data."""
    print("Memulai proses preprocessing...")
    
    # 1. Menghapus kolom yang tidak relevan
    kolom_dihapus = ['PassengerId', 'Name', 'Ticket', 'Cabin']
    # Hanya drop kolom jika ada di dalam dataframe
    df_clean = df.drop(columns=[col for col in kolom_dihapus if col in df.columns])
    
    # 2. Menangani Missing Values
    if 'Age' in df_clean.columns:
        df_clean['Age'] = df_clean['Age'].fillna(df_clean['Age'].median())
    if 'Embarked' in df_clean.columns:
        df_clean['Embarked'] = df_clean['Embarked'].fillna(df_clean['Embarked'].mode()[0])
        
    # 3. Encoding Data Kategorikal
    kolom_kategori = ['Sex', 'Embarked']
    kolom_kategori_ada = [col for col in kolom_kategori if col in df_clean.columns]
    df_clean = pd.get_dummies(df_clean, columns=kolom_kategori_ada, drop_first=True)
    
    print("Preprocessing selesai!")
    return df_clean

def save_data(df, output_path):
    """Fungsi untuk menyimpan data hasil preprocessing."""
    # Membuat direktori jika belum ada
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Data tersimpan di {output_path}")

if __name__ == "__main__":
    # Mendefinisikan path data relatif terhadap lokasi eksekusi
    # File ini idealnya dijalankan dari root folder repositori
    RAW_DATA_PATH = "../titanic.csv"
    PROCESSED_DATA_PATH = "titanicDataset_preprocessing/titanic_processed.csv"
    
    # Menjalankan alur preprocessing
    try:
        data = load_data(RAW_DATA_PATH)
        processed_data = preprocess_data(data)
        save_data(processed_data, PROCESSED_DATA_PATH)
    except Exception as e:
        print(f"Terjadi error: {e}")