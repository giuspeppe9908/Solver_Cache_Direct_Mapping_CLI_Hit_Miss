# Solver_Cache_Direct_Mapping_CLI_Hit_Miss
Risolutore per esercizi esame Arch. Elaboratori - Hit e Miss 

📌 Panoramica
Questo tool Python risolve esercizi di Architettura degli Elaboratori su cache a mappatura diretta, calcolando automaticamente:

TAG, HIT/MISS

Stato della cache dopo ogni accesso

Statistiche finali (hit rate, miss rate)

🚀 Come Usare
1. Installazione
Nessuna installazione richiesta! Basta Python 3.x:

2. Modalità Disponibili
A) Modalità Esercizio Specifico (Opzione 1)
Risolve automaticamente l'esercizio d'esempio

Indirizzi: 5 bit binari

Cache: 8 linee

Output formattato come nei testi d'esame

B) Modalità Interattiva (Opzione 2)
Per esercizi personalizzati:

Inserisci configurazione:

Bit degli indirizzi (es. 5, 8, 16)

Numero di linee cache (es. 8, 16, 32)

Inserisci sequenza di indirizzi in binario

3. Formato Input
Indirizzi: stringhe binarie (es. '10011', '01101')
Separatore: spazio
Esempio: 10011 11011 10011 01111

📊 Esempio d'Uso
Input esercizio tipico:
Indirizzi a 5 bit: 10011 11011 10011 01111 10011 01111 01111 10111 00011
Cache: 8 linee

🎯 Perché Usarlo?
✅ Risparmia tempo nei calcoli manuali
✅ Verifica immediata delle soluzioni
✅ Formato esame-ready per esercitazioni
✅ Adattabile a diverse configurazioni
✅ Spiegazione passo-passo degli accessi

⚠️ Note Importanti
Bit degli indirizzi: deve corrispondere alla lunghezza delle stringhe binarie
Numero di linee: deve essere potenza di 2 (2, 4, 8, 16...)
Cache iniziale: sempre vuota (tutte linee "non valide")

📚 Teoria di Riferimento
Il tool implementa:

Mappatura diretta: indirizzo → (tag, index, offset)
Politica di sostituzione: sempre sostituzione (unica linea possibile)
Write policy: non considerata (solo letture)

🆘 Troubleshooting
Problema: "Indirizzo non ha X bit!"
Soluzione: Assicurati che tutti gli indirizzi abbiano la stessa lunghezza

Problema: Risultati diversi dall'atteso
Soluzione: Controlla configurazione cache e interpretazione bit

Problema: Cache non si resetta
Soluzione: Usa opzione 5 (Reset) o riavvia il programma

