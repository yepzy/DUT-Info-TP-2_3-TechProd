#import importData
import bottle
import web


def main():
   #importData.importData('DB/data.db')
   
   bottle.run(host='localhost', port=8080)

# Execution de la fonction main au lancement du script
if __name__ == '__main__':
    main()
