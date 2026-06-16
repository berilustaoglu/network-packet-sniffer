import sys

# Ağ paketlerini yakalamak için ünlü Scapy kütüphanesini kullanıyoruz.
try:
    from scapy.all import sniff, IP, TCP, UDP
except ImportError:
    print("[-] Hata: 'scapy' kütüphanesi bulunamadı.")
    print("[*] Lütfen terminale şu komutu yazarak yükleyin: pip install scapy")
    sys.exit()

def banner():
    print("=" * 60)
    print("        LIGHTWEIGHT NETWORK PACKET SNIFFER (WIRESHARK-LIKE)       ")
    print("=" * 60)
    print("[*] Canlı ağ trafiği dinleniyor... (Durdurmak için: CTRL+C)\n")

def paket_yakala(packet):
    # Eğer yakalanan pakette bir IP katmanı varsa analiz et
    if packet.haslayer(IP):
        ip_layer = packet[IP]
        kaynak_ip = ip_layer.src
        hedef_ip = ip_layer.dst
        proto = "UNKNOWN"
        
        # Protokol türünü belirleme (TCP mi UDP mi?)
        if packet.haslayer(TCP):
            proto = "TCP"
        elif packet.haslayer(UDP):
            proto = "UDP"
            
        # Yakalanan paketin özetini ekrana siber güvenlik formatında yazdır
        print(f"[🌐 PACKET] [{proto}] {kaynak_ip}  --->  {hedef_ip}")

if __name__ == "__main__":
    banner()
    try:
        # Ağ kartını dinlemeye başlar. Her paket geldiğinde 'paket_yakala' fonksiyonunu çağırır.
        # 'count=0' sınırsız sayıda paket dinle anlamına gelir.
        sniff(prn=paket_yakala, store=False, count=0)
    except KeyboardInterrupt:
        print("\n[+] Dinleme kullanıcı tarafından durduruldu. Çıkılıyor...")
    except PermissionError:
        print("\n[-] Hata: Ağ kartını dinlemek için Yönetici (Administrator/Root) yetkisi gerekiyor!")
