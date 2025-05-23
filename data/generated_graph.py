node_list = [
    {"id": i, "name": name} for i, name in {
        0: "Gudang Utama", 1: "Ruko A", 2: "Toko B", 3: "Apartemen C", 4: "Mall D", 5: "Perumahan E", 6: "Pasar F",
        7: "Kantor G", 8: "SPBU H", 9: "Sekolah I", 10: "Pabrik J", 11: "Warung K", 12: "Supermarket L", 13: "Rumah M",
        14: "Klinik N", 15: "Gedung O", 16: "Taman P", 17: "Kafe Q", 18: "Hotel R", 19: "Museum S", 20: "Stasiun T",
        21: "Restoran U", 22: "Perkantoran V", 23: "Gereja W", 24: "Mesjid X", 25: "Lapangan Y", 26: "Universitas Z",
        27: "Kampus A1", 28: "Bengkel A2", 29: "Terminal A3"
    }.items()
]

edge_list = [
    {"from": 0, "to": 1, "distance": 2.5, "speed": 40, "congestion": 0.3, "oneway": False},
    {"from": 0, "to": 2, "distance": 3.2, "speed": 35, "congestion": 0.4, "oneway": False},
    {"from": 1, "to": 3, "distance": 1.8, "speed": 30, "congestion": 0.5, "oneway": True},
    {"from": 2, "to": 4, "distance": 2.0, "speed": 45, "congestion": 0.2, "oneway": False},
    {"from": 3, "to": 5, "distance": 2.3, "speed": 25, "congestion": 0.6, "oneway": False},
    {"from": 5, "to": 7, "distance": 2.2, "speed": 20, "congestion": 0.7, "oneway": True},
    {"from": 6, "to": 8, "distance": 1.5, "speed": 40, "congestion": 0.3, "oneway": False},
    {"from": 8, "to": 10, "distance": 2.1, "speed": 45, "congestion": 0.2, "oneway": True},
    {"from": 10, "to": 12, "distance": 2.6, "speed": 50, "congestion": 0.3, "oneway": False},
    {"from": 12, "to": 14, "distance": 2.9, "speed": 40, "congestion": 0.2, "oneway": False},
    {"from": 14, "to": 16, "distance": 2.3, "speed": 30, "congestion": 0.5, "oneway": True},
    {"from": 16, "to": 18, "distance": 1.9, "speed": 50, "congestion": 0.3, "oneway": False},
    {"from": 18, "to": 20, "distance": 2.7, "speed": 30, "congestion": 0.4, "oneway": False},
    {"from": 20, "to": 22, "distance": 1.6, "speed": 50, "congestion": 0.2, "oneway": False},
    {"from": 22, "to": 24, "distance": 1.8, "speed": 25, "congestion": 0.7, "oneway": False},
    {"from": 24, "to": 26, "distance": 2.5, "speed": 45, "congestion": 0.2, "oneway": False},
    {"from": 26, "to": 28, "distance": 2.0, "speed": 30, "congestion": 0.5, "oneway": False},
    {"from": 28, "to": 0, "distance": 3.0, "speed": 50, "congestion": 0.1, "oneway": False},
    {"from": 1, "to": 6, "distance": 2.7, "speed": 40, "congestion": 0.3, "oneway": False},
    {"from": 2, "to": 7, "distance": 2.4, "speed": 35, "congestion": 0.4, "oneway": False},
    {"from": 3, "to": 8, "distance": 2.2, "speed": 30, "congestion": 0.5, "oneway": True},
    {"from": 4, "to": 9, "distance": 1.8, "speed": 45, "congestion": 0.2, "oneway": False},
    {"from": 5, "to": 10, "distance": 3.0, "speed": 50, "congestion": 0.3, "oneway": False},
    {"from": 6, "to": 11, "distance": 2.1, "speed": 40, "congestion": 0.4, "oneway": False},
    {"from": 7, "to": 12, "distance": 1.9, "speed": 30, "congestion": 0.6, "oneway": False},
    {"from": 8, "to": 13, "distance": 2.5, "speed": 35, "congestion": 0.5, "oneway": True},
    {"from": 9, "to": 14, "distance": 3.3, "speed": 40, "congestion": 0.3, "oneway": False},
    {"from": 10, "to": 15, "distance": 1.7, "speed": 25, "congestion": 0.7, "oneway": False},
    {"from": 11, "to": 16, "distance": 2.6, "speed": 30, "congestion": 0.3, "oneway": False},
    {"from": 12, "to": 17, "distance": 2.4, "speed": 45, "congestion": 0.2, "oneway": False},
    {"from": 13, "to": 18, "distance": 3.0, "speed": 50, "congestion": 0.4, "oneway": False},
    {"from": 14, "to": 19, "distance": 1.6, "speed": 35, "congestion": 0.6, "oneway": False},
    {"from": 15, "to": 20, "distance": 2.0, "speed": 40, "congestion": 0.3, "oneway": False},
    {"from": 16, "to": 21, "distance": 2.8, "speed": 30, "congestion": 0.5, "oneway": False},
    {"from": 17, "to": 22, "distance": 2.9, "speed": 25, "congestion": 0.4, "oneway": False},
    {"from": 18, "to": 23, "distance": 1.5, "speed": 35, "congestion": 0.3, "oneway": True},
    {"from": 19, "to": 24, "distance": 3.1, "speed": 40, "congestion": 0.2, "oneway": False},
    {"from": 20, "to": 25, "distance": 2.2, "speed": 45, "congestion": 0.5, "oneway": False}
]