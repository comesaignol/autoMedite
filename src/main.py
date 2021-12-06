# General
import argparse

# AutoMedite
import xml2txt
import alignmentRaw
import alignmentCorr
import alignmentTei
import interface


def main():
  parser = argparse.ArgumentParser()
  
  
  parser.add_argument("-o",
                      "--option",
                      help="Option for autoMedite",
                      required=True,
                      )
  
  parser.add_argument("-t1",
                      "--text1",
                      help="Select text1",
                      required=False,
                      )
  
  parser.add_argument("-t2",
                      "--text2",
                      help="Select text2",
                      required=False,
                      )
  
  parser.add_argument("-c",
                      "--casse",
                      help="Select option casse",
                      required=False,
                      )
  
  parser.add_argument("-s",
                      "--separator",
                      help="Select option separator",
                      required=False,
                      )
  
  parser.add_argument("-d",
                      "--diacritique",
                      help="Select option diacritique",
                      required=False,
                      )
  
  parser.add_argument("-w",
                      "--word",
                      help="Select option word",
                      required=False,
                      )

  args = parser.parse_args()
  option = args.option
  text1 = args.text1
  text2 = args.text2
  casse = args.casse
  separator = args.separator
  diacritique = args.diacritique
  word = args.word
  
  
  optionList = ["xml2txt", "alignmentRaw", "alignmentCorr", "alignmentTei", "interface"]
  if option not in optionList:
    print("Error: the option argument is invalid. Please, use option 'xml2txt'")
  else:
    
    # xml2txt
    if option == "xml2txt":
      if text1 and text2:
        xml2txt.main(text1, text2)
      else:
        print("Error: the option argument is invalid. Please, enter param t1 et param t2")
        
    # alignmentRaw
    if option == "alignmentRaw":
      if text1 and text2 and casse and separator and diacritique and word:
        alignmentRaw.main(text1=text1, text2=text2, casse=casse, separator=separator, diacritique=diacritique, word=word)
      else:
        print("Error: the option argument is invalid. Please, enter param t1 et param t2")
    
    # alignmentCorr
    if option == "alignmentCorr":
      if text1 and text2:
        alignmentCorr.main(text1=text1, text2=text2)
      else:
        print("Error: the option argument is invalid. Please, enter param t1 et param t2")
    
    # alignmentTei
    if option == "alignmentTei":
      if text1 and text2:
        alignmentTei.main(text1=text1, text2=text2)
      else:
        print("Error: the option argument is invalid. Please, enter param t1 et param t2")
    
    # interface
    if option == "interface":
      if text1 and text2:
        interface.main(text1=text1, text2=text2)
      else:
        print("Error: the option argument is invalid. Please, enter param t1 et param t2")

main()