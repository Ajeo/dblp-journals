# DBLP journals

Execute LDA algorithm, using tmt-0.4.0, for ACM Transaction and IEE Transaction journals 

## First run, parser_for_journals.py

    python scripts/parser_for_journals.py

## Second, split journals csv in csv for journal

    python scripts/split_journals_files.py

## Third, run tmt for each journal

    python scripts/run_tmt.py
