sibal_textlist = []

class fuck:
  def Returnlist():
    return sibal_textlist
  def NOOOO(repitedlist):
    for commentsdict in repitedlist:
      textelement = commentsdict.get("text")
      Author = commentsdict.get("author")
      if Author == None or Author == "None":
        sibal_textlist.append("[삭제된 글입니다 | DELETED]")
      else : sibal_textlist.append(f'<h1>ㄴ1번째 대댓글 | Reply level 1 _____Writer: {Author}_____</h1>\n{textelement}')
      repitedlist = commentsdict.get('children')
      for commentsdict in repitedlist:
        textelement = commentsdict.get("text")
        Author = commentsdict.get("author")
        if Author == None or Author == "None":
          sibal_textlist.append("[삭제된 글입니다 | DELETED]")
        else : sibal_textlist.append(f'<h1>ㄴ2번째 대댓글 | Reply level 2 _____Writer: {Author}_____</h1>\n{textelement}')
        repitedlist = commentsdict.get('children')
        for commentsdict in repitedlist:
          textelement = commentsdict.get("text")
          Author = commentsdict.get("author")
          if Author == None or Author == "None":
            sibal_textlist.append("[삭제된 글입니다 | DELETED]")
          else : sibal_textlist.append(f'<h1>ㄴ3번째 대댓글 | Reply level 3 _____Writer: {Author}_____</h1>\n{textelement}')
          repitedlist = commentsdict.get('children')
          for commentsdict in repitedlist:
            textelement = commentsdict.get("text")
            Author = commentsdict.get("author")
            if Author == None or Author == "None":
              sibal_textlist.append("[삭제된 글입니다 | DELETED]")
            else : sibal_textlist.append(f'<h1>ㄴ4번째 대댓글 | Reply level 4 _____Writer: {Author}_____</h1>\n{textelement}')
            repitedlist = commentsdict.get('children')
            for commentsdict in repitedlist:
              textelement = commentsdict.get("text")
              Author = commentsdict.get("author")
              if Author == None or Author == "None":
                sibal_textlist.append("[삭제된 글입니다 | DELETED]")
              else : sibal_textlist.append(f'<h1>ㄴ5번째 대댓글 | Reply level 5 _____Writer: {Author}_____</h1>\n{textelement}')
              repitedlist = commentsdict.get('children')
              for commentsdict in repitedlist:
                textelement = commentsdict.get("text")
                Author = commentsdict.get("author")
                if Author == None or Author == "None":
                  sibal_textlist.append("[삭제된 글입니다 | DELETED]")
                else : sibal_textlist.append(f'<h1>ㄴ6번째 대댓글 | Reply level 6 _____Writer: {Author}_____</h1>\n{textelement}')
                repitedlist = commentsdict.get('children')
                for commentsdict in repitedlist:
                  textelement = commentsdict.get("text")
                  Author = commentsdict.get("author")
                  if Author == None or Author == "None":
                    sibal_textlist.append("[삭제된 글입니다 | DELETED]")
                  else : sibal_textlist.append(f'<h1>ㄴ7번째 대댓글 | Reply level 7 _____Writer: {Author}_____</h1>\n{textelement}')
                  repitedlist = commentsdict.get('children')
                  for commentsdict in repitedlist:
                    textelement = commentsdict.get("text")
                    Author = commentsdict.get("author")
                    if Author == None or Author == "None":
                      sibal_textlist.append("[삭제된 글입니다 | DELETED]")
                    else : sibal_textlist.append(f'<h1>ㄴ8번째 대댓글 | Reply level 8 _____Writer: {Author}_____</h1>\n{textelement}')
                    repitedlist = commentsdict.get('children')
                    for commentsdict in repitedlist:
                      textelement = commentsdict.get("text")
                      Author = commentsdict.get("author")
                      if Author == None or Author == "None":
                        sibal_textlist.append("[삭제된 글입니다 | DELETED]")
                      else : sibal_textlist.append(f'<h1>ㄴ9번째 대댓글 | Reply level 9 _____Writer: {Author}_____</h1>\n{textelement}')
                      repitedlist = commentsdict.get('children')
                      for commentsdict in repitedlist:
                        textelement = commentsdict.get("text")
                        Author = commentsdict.get("author")
                        if Author == None or Author == "None":
                          sibal_textlist.append("[삭제된 글입니다 | DELETED]")
                        else : sibal_textlist.append(f'<h1>ㄴ10번째 대댓글 | Reply level 10 _____Writer: {Author}_____</h1>\n{textelement}')
                        repitedlist = commentsdict.get('children')