import importData
import REST.restServeur


def main():
   importData.importData('DB/data.db')
   restServeur.main()

# Execution de la fonction main au lancement du script
if __name__ == '__main__':
    main()
