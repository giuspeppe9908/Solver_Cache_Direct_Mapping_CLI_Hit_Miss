class DirectMappedCacheSolver:
    def __init__(self, address_bits=5, num_lines=8):
        """
        Risolutore per cache a mappatura diretta con indirizzi binari
        
        Args:
            address_bits: numero di bit degli indirizzi (default: 5)
            num_lines: numero di linee nella cache (default: 8, cioè 2³)
        """
        self.address_bits = address_bits
        self.num_lines = num_lines
        
        # Calcola bit per index e tag
        # index_bits = log2(num_lines)
        self.index_bits = (num_lines - 1).bit_length()  # log2(num_lines)
        self.offset_bits = 0  # In questi esercizi spesso non c'è offset, solo tag e index
        self.tag_bits = address_bits - self.index_bits
        
        # Inizializza cache: ogni linea ha (valid, tag)
        self.cache = [{'valid': False, 'tag': None} for _ in range(num_lines)]
        
        # Storico accessi
        self.history = []
        self.hits = 0
        self.misses = 0
        
    def parse_address(self, address_bin):
        """
        Scompone un indirizzo binario in tag e index
        
        Args:
            address_bin: stringa binaria (es. '10011')
        
        Returns:
            (index_dec, index_bin, tag_bin)
        """
        # Assicuriamoci che l'indirizzo sia della lunghezza corretta
        if len(address_bin) != self.address_bits:
            # Completa con zeri a sinistra se necessario
            address_bin = address_bin.zfill(self.address_bits)
        
        # Estrai index (bit meno significativi)
        # index_bits = log2(num_lines)
        index_bin = address_bin[-self.index_bits:] if self.index_bits > 0 else '0'
        tag_bin = address_bin[:-self.index_bits] if self.index_bits > 0 else address_bin
        
        # Converti index in decimale
        index_dec = int(index_bin, 2) if index_bin else 0
        
        return index_dec, index_bin, tag_bin
    
    def access(self, address_bin):
        """
        Simula un accesso alla cache
        
        Args:
            address_bin: indirizzo binario (es. '10011')
        
        Returns:
            'HIT' o 'MISS'
        """
        index_dec, index_bin, tag_bin = self.parse_address(address_bin)
        
        line = self.cache[index_dec]
        
        # Aggiungi allo storico
        access_info = {
            'address': address_bin,
            'index_bin': index_bin,
            'index_dec': index_dec,
            'tag': tag_bin
        }
        
        if line['valid'] and line['tag'] == tag_bin:
            # HIT
            self.hits += 1
            access_info['result'] = 'HIT'
            access_info['action'] = 'Nessuna modifica'
        else:
            # MISS - aggiorna la linea
            self.misses += 1
            line['valid'] = True
            line['tag'] = tag_bin
            access_info['result'] = 'MISS'
            access_info['action'] = f'Sostituito tag {line["tag"]}'
        
        self.history.append(access_info)
        return access_info['result']
    
    def analyze_sequence(self, addresses):
        """
        Analizza una sequenza di indirizzi
        
        Args:
            addresses: lista di stringhe binarie
        
        Returns:
            Lista di risultati dettagliati
        """
        results = []
        for addr in addresses:
            result = self.access(addr)
            results.append((addr, result))
        return results
    
    def get_cache_state(self):
        """
        Restituisce lo stato corrente della cache
        
        Returns:
            Lista di tuple (linea, tag o "Non valido")
        """
        state = []
        for i, line in enumerate(self.cache):
            if line['valid']:
                # Converti index in binario con padding appropriato
                index_bin = format(i, f'0{self.index_bits}b')
                state.append((index_bin, line['tag']))
            else:
                index_bin = format(i, f'0{self.index_bits}b')
                state.append((index_bin, "Non valido"))
        return state
    
    def print_detailed_analysis(self):
        """Stampa analisi dettagliata"""
        print("=" * 70)
        print("ANALISI DETTAGLIATA - CACHE A MAPPATURA DIRETTA")
        print("=" * 70)
        print(f"Bit indirizzo: {self.address_bits}")
        print(f"Numero linee: {self.num_lines}")
        print(f"Bit index: {self.index_bits}")
        print(f"Bit tag: {self.tag_bits}")
        print()
        
        print("SEQUENZA DI ACCESSI:")
        print("Richiesta | Indirizzo | Index | Tag  | Risultato | Azione")
        print("-" * 65)
        
        for i, access in enumerate(self.history, 1):
            print(f"{i:8d} | {access['address']:^9s} | {access['index_bin']:^5s} | "
                  f"{access['tag']:^4s} | {access['result']:^8s} | {access['action']}")
        
        print("\n" + "=" * 70)
        print("STATO FINALE DELLA CACHE:")
        print("=" * 70)
        print("Linea (bin) | Tag memorizzato / Stato")
        print("-" * 40)
        
        for i, line in enumerate(self.cache):
            index_bin = format(i, f'0{self.index_bits}b')
            if line['valid']:
                print(f"     {index_bin}     | {line['tag']}")
            else:
                print(f"     {index_bin}     | Non valido")
        
        print("\n" + "=" * 70)
        print("STATISTICHE:")
        print("=" * 70)
        print(f"HIT:  {self.hits}")
        print(f"MISS: {self.misses}")
        print(f"Totale accessi: {self.hits + self.misses}")
        if (self.hits + self.misses) > 0:
            hit_rate = self.hits / (self.hits + self.misses)
            print(f"Hit rate: {hit_rate:.2%}")
    
    def reset(self):
        """Resetta la cache"""
        self.cache = [{'valid': False, 'tag': None} for _ in range(self.num_lines)]
        self.history = []
        self.hits = 0
        self.misses = 0


def solve_specific_exercise():
    """Risolve l'esercizio specifico che hai fornito"""
    print("=" * 70)
    print("RISOLUZIONE ESERCIZIO SPECIFICO")
    print("=" * 70)
    
    # Configurazione dell'esercizio
    address_bits = 5  # Indirizzi a 5 bit
    num_lines = 8     # 8 linee nella cache
    
    solver = DirectMappedCacheSolver(address_bits, num_lines)
    
    # Sequenza dell'esercizio
    sequence = [
        '10011',
        '11011',
        '10011',
        '01111',
        '10011',
        '01111',
        '01111',
        '10111',
        '00011'
    ]
    
    print(f"Sequenza di indirizzi: {sequence}")
    print()
    
    # Analizza la sequenza
    solver.analyze_sequence(sequence)
    
    # Stampa risultati
    solver.print_detailed_analysis()
    
    # Confronto con le tue risposte
    print("\n" + "=" * 70)
    print("CONFRONTO CON LE TUE RISPOSTE:")
    print("=" * 70)
    
    cache_state = solver.get_cache_state()
    print("\nTabella cache completata:")
    for index_bin, tag in cache_state:
        if tag == "Non valido":
            print(f"Linea {index_bin}: Non valido/Invalid")
        else:
            print(f"Linea {index_bin}: Tag: {tag}")
    
    print(f"\nHit: {solver.hits} (tu hai indicato: 3)")
    print(f"Miss: {solver.misses} (tu hai indicato: 6)")
    
    if solver.hits == 3 and solver.misses == 6:
        print("\n✓ Le tue risposte sono CORRETTE!")
    else:
        print("\n✗ ATTENZIONE: c'è una discrepanza con le tue risposte")


def interactive_solver():
    """Risolutore interattivo per esercizi generici"""
    print("=" * 70)
    print("RISOLUTORE INTERATTIVO PER ESERCIZI CACHE")
    print("=" * 70)
    
    print("\nCONFIGURAZIONE:")
    address_bits = int(input("Numero di bit degli indirizzi (es. 5, 8, 16): "))
    num_lines = int(input("Numero di linee nella cache (es. 8, 16, 32): "))
    
    solver = DirectMappedCacheSolver(address_bits, num_lines)
    
    while True:
        print("\n" + "=" * 50)
        print("MENU:")
        print("1. Inserisci sequenza di indirizzi")
        print("2. Analizza singolo indirizzo")
        print("3. Visualizza stato cache")
        print("4. Mostra analisi completa")
        print("5. Nuovo esercizio (reset)")
        print("6. Esci")
        
        choice = input("\nScelta: ").strip()
        
        if choice == '1':
            seq_input = input("Inserisci sequenza di indirizzi binari (separati da spazio): ").strip()
            addresses = seq_input.split()
            
            # Verifica che tutti gli indirizzi abbiano la lunghezza corretta
            valid = True
            for addr in addresses:
                if len(addr) != address_bits:
                    print(f"ATTENZIONE: l'indirizzo {addr} non ha {address_bits} bit!")
                    valid = False
            
            if valid:
                solver.reset()
                solver.analyze_sequence(addresses)
                print(f"\nSequenza analizzata: {len(addresses)} accessi")
                
                # Mostra sommario
                print(f"\nSommario: {solver.hits} HIT, {solver.misses} MISS")
                
                # Mostra tabella cache
                print("\nStato cache attuale:")
                cache_state = solver.get_cache_state()
                for index_bin, tag in cache_state:
                    if tag == "Non valido":
                        print(f"Linea {index_bin}: Non valido")
                    else:
                        print(f"Linea {index_bin}: Tag: {tag}")
        
        elif choice == '2':
            addr = input("Indirizzo binario: ").strip()
            
            if len(addr) != address_bits:
                print(f"L'indirizzo deve avere {address_bits} bit!")
                if len(addr) < address_bits:
                    addr = addr.zfill(address_bits)
                    print(f"Ho completato con zeri: {addr}")
            
            result = solver.access(addr)
            index_dec, index_bin, tag_bin = solver.parse_address(addr)
            
            print(f"\nIndirizzo: {addr}")
            print(f"Index (bin): {index_bin} (dec: {index_dec})")
            print(f"Tag: {tag_bin}")
            print(f"Risultato: {result}")
        
        elif choice == '3':
            print("\nSTATO CACHE ATTUALE:")
            cache_state = solver.get_cache_state()
            for index_bin, tag in cache_state:
                if tag == "Non valido":
                    print(f"Linea {index_bin}: Non valido")
                else:
                    print(f"Linea {index_bin}: Tag: {tag}")
        
        elif choice == '4':
            if solver.history:
                solver.print_detailed_analysis()
            else:
                print("Nessun accesso effettuato ancora!")
        
        elif choice == '5':
            solver.reset()
            print("Cache resettata. Pronto per nuovo esercizio.")
        
        elif choice == '6':
            print("Arrivederci!")
            break
        
        else:
            print("Scelta non valida!")


# Main
if __name__ == "__main__":
    print("RISOLUTORE ESERCIZI CACHE - MAPPATURA DIRETTA")
    print("=" * 70)
    
    print("\nScegli modalità:")
    print("1. Risolvi l'esercizio specifico (indirizzi 5 bit, 8 linee)")
    print("2. Modalità interattiva per esercizi generici")
    print("3. Test con altri esempi")
    
    mode = input("\nScelta (1, 2 o 3): ").strip()
    
    if mode == '1':
        solve_specific_exercise()
    elif mode == '2':
        interactive_solver()
    elif mode == '3':
        # Altri esempi di test
        print("\nTest con cache 4 linee, indirizzi 4 bit:")
        test_solver = DirectMappedCacheSolver(4, 4)
        test_seq = ['0000', '0100', '0000', '1100', '0000']
        test_solver.analyze_sequence(test_seq)
        test_solver.print_detailed_analysis()
    else:
        print("Modalità non riconosciuta!")