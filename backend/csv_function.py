import os
import pandas as pd
import csv

def file_check(file_path,dbx_path, dbx,index1):
  try:
    if not os.path.isfile(file_path):
      with open(file_path, 'w') as f:
          writer = csv.writer(f)
          writer.writerow(index1)
      dbx.files_upload(open(file_path, 'rb').read(), dbx_path)
      return False, []
    else:
        os.remove(file_path)
        dbx.files_download_to_file(file_path, dbx_path)
        return False,[]
  except Exception as e:
    return True, ['csv_upload_error:'+str(e)]

def file_update(file_path,dbx_path,dbx,column,add_list):
  df = pd.read_csv(file_path)
  add_df = pd.DataFrame(add_list,columns=column)
  updated_df = pd.concat([df,add_df],ignore_index=True)
  updated_df.to_csv(file_path, index = False)

  dbx.files_delete(dbx_path)

  dbx.files_upload(open(file_path, 'rb').read(), dbx_path)