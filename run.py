import os
import requests
import re
import pandas as pd
import numpy as np
from pycaret.classification import load_model, predict_model
import gradio as gr
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages



source_best_model_pkl = './baba_vanga_v1.pkl'
font = './Roboto-Regular.ttf'


headers = {'Accept': 'application/json'}



def get_season_id_from_url(url):
  html = requests.get(url).text
  return re.search(r'seasonId=(\d+)&type=', html).group(1)

def cek(ligid, kacincihafta):
    df = pd.DataFrame(columns=['name', 'evyuzdelikdilim',
                               'depyuzdelikdilim', 'evims', 'depims', 'evdms', 'depdms', 'evig',
                               'depig', 'evdg', 'depdg', 'evib', 'depib', 'evdb', 'depdb', 'evim',
                               'depim', 'evdm', 'depdm', 'eviag', 'depiag', 'evdag', 'depdag', 'eviyg',
                               'depiyg', 'evdyg', 'depdyg', 'evip', 'depip', 'evdp', 'depdp'])
    puandurumu = pd.read_csv("./standings.csv", skipinitialspace=True, na_values="?", comment="\t", sep=",", low_memory=False)
    sonhaftamaclari = requests.get(
        'https://arsiv.mackolik.com/Standings/Data/WeeklyStandingData.aspx?seas=' + str(ligid) + '&hft=' + str(
            kacincihafta), headers=headers)
    sonhaftamaclari = sonhaftamaclari.json()
    for maclar in sonhaftamaclari["d"]:
        if maclar[2] != "MS":
            evid = maclar[3]
            depid = maclar[4]
            evadi = puandurumu.loc[puandurumu['evtakimid'] == evid, 'evtakimadi'].iloc[0]
            depadi = puandurumu.loc[puandurumu['deptakimid'] == depid, 'deptakimadi'].iloc[0]
            macadi = str(evadi) + " - " + str(depadi)
            evyuzdelikdilim = puandurumu.loc[puandurumu['evtakimid'] == evid, 'evyuzdelikdilim'].iloc[0]
            evims = puandurumu.loc[puandurumu['evtakimid'] == evid, 'evims'].iloc[0]
            evdms = puandurumu.loc[puandurumu['evtakimid'] == evid, 'evdms'].iloc[0]
            evig = puandurumu.loc[puandurumu['evtakimid'] == evid, 'evig'].iloc[0]
            evib = puandurumu.loc[puandurumu['evtakimid'] == evid, 'evib'].iloc[0]
            evim = puandurumu.loc[puandurumu['evtakimid'] == evid, 'evim'].iloc[0]
            evdg = puandurumu.loc[puandurumu['evtakimid'] == evid, 'evdg'].iloc[0]
            evdb = puandurumu.loc[puandurumu['evtakimid'] == evid, 'evdb'].iloc[0]
            evdm = puandurumu.loc[puandurumu['evtakimid'] == evid, 'evdm'].iloc[0]
            eviag = puandurumu.loc[puandurumu['evtakimid'] == evid, 'eviag'].iloc[0]
            eviyg = puandurumu.loc[puandurumu['evtakimid'] == evid, 'eviyg'].iloc[0]
            evdag = puandurumu.loc[puandurumu['evtakimid'] == evid, 'evdag'].iloc[0]
            evdyg = puandurumu.loc[puandurumu['evtakimid'] == evid, 'evdyg'].iloc[0]
            evip = puandurumu.loc[puandurumu['evtakimid'] == evid, 'evip'].iloc[0]
            evdp = puandurumu.loc[puandurumu['evtakimid'] == evid, 'evdp'].iloc[0]
            depyuzdelikdilim = puandurumu.loc[puandurumu['deptakimid'] == depid, 'depyuzdelikdilim'].iloc[0]
            depims = puandurumu.loc[puandurumu['deptakimid'] == depid, 'depims'].iloc[0]
            depdms = puandurumu.loc[puandurumu['deptakimid'] == depid, 'depdms'].iloc[0]
            depig = puandurumu.loc[puandurumu['deptakimid'] == depid, 'depig'].iloc[0]
            depib = puandurumu.loc[puandurumu['deptakimid'] == depid, 'depib'].iloc[0]
            depim = puandurumu.loc[puandurumu['deptakimid'] == depid, 'depim'].iloc[0]
            depdg = puandurumu.loc[puandurumu['deptakimid'] == depid, 'depdg'].iloc[0]
            depdb = puandurumu.loc[puandurumu['deptakimid'] == depid, 'depdb'].iloc[0]
            depdm = puandurumu.loc[puandurumu['deptakimid'] == depid, 'depdm'].iloc[0]
            depiag = puandurumu.loc[puandurumu['deptakimid'] == depid, 'depiag'].iloc[0]
            depiyg = puandurumu.loc[puandurumu['deptakimid'] == depid, 'depiyg'].iloc[0]
            depdag = puandurumu.loc[puandurumu['deptakimid'] == depid, 'depdag'].iloc[0]
            depdyg = puandurumu.loc[puandurumu['deptakimid'] == depid, 'depdyg'].iloc[0]
            depip = puandurumu.loc[puandurumu['deptakimid'] == depid, 'depip'].iloc[0]
            depdp = puandurumu.loc[puandurumu['deptakimid'] == depid, 'depdp'].iloc[0]
            ekleneceksatir = {"name": str(macadi), "evyuzdelikdilim": str(evyuzdelikdilim), "depyuzdelikdilim": str(depyuzdelikdilim), "evims": str(evims), "depims": str(depims), "evdms": str(evdms), "depdms": str(depdms), "evig": str(evig), "depig": str(depig), "evdg": str(evdg), "depdg": str(depdg), "evib": str(evib), "depib": str(depib), "evdb": str(evdb), "depdb": str(depdb), "evim": str(evim), "depim": str(depim), "evdm": str(evdm), "depdm": str(depdm), "eviag": str(eviag), "depiag": str(depiag), "evdag": str(evdag), "depdag": str(depdag), "eviyg": str(eviyg), "depiyg": str(depiyg), "evdyg": str(evdyg), "depdyg": str(depdyg), "evip": str(evip), "depip": str(depip), "evdp": str(evdp), "depdp": str(depdp)}
            df = pd.concat([df, pd.DataFrame([ekleneceksatir])], ignore_index=True)

    if os.path.isfile('./matches.csv'):
        df.to_csv('matches.csv', mode='a', header=False)
    else:
        df.to_csv('matches.csv')

def hazirla(ligid, kacincihafta):
    puandf = pd.DataFrame(
        columns=['takimid', 'takimadi', 'ims', 'dms', 'ig', 'dg', 'ib', 'db', 'im', 'dm', 'iag', 'dag', 'iyg', 'dyg',
                 'ip', 'dp'])
    puandurumu = requests.get(
        'https://arsiv.mackolik.com/AjaxHandlers/StandingHandler.ashx?op=standing&id=' + str(ligid), headers=headers)
    puandurumu = puandurumu.json()
    for takim in puandurumu["s"]:
        takimid = takim[0]
        takimadi = takim[1]
        ims = takim[2]
        dms = takim[3]
        ig = takim[4]
        dg = takim[5]
        ib = takim[6]
        db = takim[7]
        im = takim[8]
        dm = takim[9]
        iag = takim[10]
        dag = takim[11]
        iyg = takim[12]
        dyg = takim[13]
        ip = takim[14]
        dp = takim[15]
        ekleneceksatir = pd.DataFrame(
            [[takimid, takimadi, ims, dms, ig, dg, ib, db, im, dm, iag, dag, iyg, dyg, ip, dp]], columns=puandf.columns)
        puandf = pd.concat([puandf, ekleneceksatir], ignore_index=True)

    sonhaftamaclari = requests.get(
        'https://arsiv.mackolik.com/Standings/Data/WeeklyStandingData.aspx?seas=' + str(ligid) + '&hft=' + str(
            kacincihafta), headers=headers)
    sonhaftamaclari = sonhaftamaclari.json()
    for maclar in sonhaftamaclari["d"]:
        if maclar[2] == "MS":
            evid = maclar[3]
            depid = maclar[4]
            evgol = maclar[6]
            depgol = maclar[7]
            if evgol > depgol:
                puandf.loc[puandf['takimid'] == evid, 'ims'] -= 1
                puandf.loc[puandf['takimid'] == evid, 'ig'] -= 1
                puandf.loc[puandf['takimid'] == evid, 'iag'] -= evgol
                puandf.loc[puandf['takimid'] == evid, 'iyg'] -= depgol
                puandf.loc[puandf['takimid'] == evid, 'ip'] -= 3
                puandf.loc[puandf['takimid'] == depid, 'dms'] -= 1
                puandf.loc[puandf['takimid'] == depid, 'dm'] -= 1
                puandf.loc[puandf['takimid'] == depid, 'dag'] -= depgol
                puandf.loc[puandf['takimid'] == depid, 'dyg'] -= evgol
            if evgol == depgol:
                puandf.loc[puandf['takimid'] == evid, 'ims'] -= 1
                puandf.loc[puandf['takimid'] == evid, 'ib'] -= 1
                puandf.loc[puandf['takimid'] == evid, 'iag'] -= evgol
                puandf.loc[puandf['takimid'] == evid, 'iyg'] -= depgol
                puandf.loc[puandf['takimid'] == evid, 'ip'] -= 1
                puandf.loc[puandf['takimid'] == depid, 'dms'] -= 1
                puandf.loc[puandf['takimid'] == depid, 'db'] -= 1
                puandf.loc[puandf['takimid'] == depid, 'dag'] -= depgol
                puandf.loc[puandf['takimid'] == depid, 'dyg'] -= evgol
                puandf.loc[puandf['takimid'] == depid, 'dp'] -= 1
            if evgol < depgol:
                puandf.loc[puandf['takimid'] == evid, 'ims'] -= 1
                puandf.loc[puandf['takimid'] == evid, 'im'] -= 1
                puandf.loc[puandf['takimid'] == evid, 'iag'] -= evgol
                puandf.loc[puandf['takimid'] == evid, 'iyg'] -= depgol
                puandf.loc[puandf['takimid'] == depid, 'dms'] -= 1
                puandf.loc[puandf['takimid'] == depid, 'dg'] -= 1
                puandf.loc[puandf['takimid'] == depid, 'dag'] -= depgol
                puandf.loc[puandf['takimid'] == depid, 'dyg'] -= evgol
                puandf.loc[puandf['takimid'] == depid, 'dp'] -= 3

    puandf["toplampuan"] = puandf["ip"] + puandf["dp"]
    puandf = puandf.sort_values(by='toplampuan', ascending=False)
    puandf['yuzdelikdilim'] = (puandf.index + 1) * 100 / len(puandf)
    evdf = puandf.add_prefix('ev')
    depdf = puandf.add_prefix('dep')
    result = pd.concat([evdf, depdf], axis=1)
    result.to_csv("standings.csv")


def tahmin():
    model = load_model('baba_vanga_v1')
    veriseti = pd.read_csv("./matches.csv", skipinitialspace=True, na_values="?", comment="\t", sep=",", low_memory=False)
    veriseti.isna().sum()
    veriseti = veriseti.dropna()
    veriseti = veriseti.reset_index(drop=True)
    verisetimacadli = veriseti
    veriseti = veriseti[['evyuzdelikdilim',
       'depyuzdelikdilim', 'evims', 'depims', 'evdms', 'depdms', 'evig',
       'depig', 'evdg', 'depdg', 'evib', 'depib', 'evdb', 'depdb', 'evim',
       'depim', 'evdm', 'depdm', 'eviag', 'depiag', 'evdag', 'depdag', 'eviyg',
       'depiyg', 'evdyg', 'depdyg', 'evip', 'depip', 'evdp', 'depdp']]
    dfcikti = predict_model(model, data=veriseti, raw_score=True)
    dfcikti = dfcikti.rename(columns={
        'prediction_score_0': 'home',
        'prediction_score_1': 'draw',
        'prediction_score_2': 'away'
    })
    dfcikti = dfcikti[['home', 'draw', 'away']]
    sontablo = pd.merge(verisetimacadli, dfcikti, left_index=True, right_index=True)
    sontablo.to_csv("result.csv", index=False)




def generate_pdf_from_dataframe(dataframe: pd.DataFrame):
    if dataframe.empty:
        print("PDF cannot be generated for an empty DataFrame.")
        return None

    pdf_file_path = "siralanmis_tahmin_tablosu.pdf"

    try:
        with PdfPages(pdf_file_path) as pdf:
            fig, ax = plt.subplots(figsize=(11, 8))
            ax.axis('off')

            table = ax.table(cellText=dataframe.values,
                             colLabels=dataframe.columns,
                             loc='center',
                             cellLoc='center',
                             rowLoc='center')

            table.auto_set_font_size(False)
            table.set_fontsize(10)
            table.scale(1.2, 1.2)

            plt.title("Baba Vanga Ai Prediction Table", fontsize=16, pad=20)
            plt.tight_layout()
            pdf.savefig(fig)
            plt.close(fig)

        return pdf_file_path
    except Exception as e:
        print(f"An error occurred while creating the PDF: {e}")
        return None




def gradio_interface():
    with gr.Blocks(title="Baba Vanga Ai") as blc:
        gr.HTML("<center><h1>Baba Vanga Ai</h1></center>")
        gr.HTML("<style>#predbutton{background-color: orange; color: white;}</style>")
        gr.HTML("<b>URL: <a href='https://arsiv.mackolik.com/Canli-Sonuclar' target='_blank'>https://arsiv.mackolik.com/Canli-Sonuclar</a>")

        ligurl = gr.Textbox(label="League Standings Url:")
        kacincihafta = gr.Textbox(label="Week Number:")
        submit_btn = gr.Button("Predict", elem_id="predbutton")
        clear_btn = gr.Button("Clear")

        tahmintablosu = gr.DataFrame(label="Predictions Table", interactive=True)

        pdf_download_button = gr.Button("Download PDF")
        pdf_output_file = gr.File(label="PDF File")

        def clearfunc():
            for f in ["./standings.csv", "./result.csv", "./matches.csv", "./siralanmis_tahmin_tablosu.pdf"]:
                try:
                    if os.path.exists(f):
                        os.remove(f)
                except Exception as e:
                    print(f"An error occurred while deleting the file: {f} - {e}")
            return pd.DataFrame(), None

        def on_submit(ligurl, kacincihafta):
            ligid = get_season_id_from_url(ligurl)
            if ligid is None:
                gr.Error("Invalid League URL or League ID not found.")
                return pd.DataFrame()

            hazirla(ligid, kacincihafta)
            cek(ligid, kacincihafta)
            tahmin()

            if not os.path.exists("./result.csv"):
                gr.Error("Failed to create prediction file (result.csv).")
                return pd.DataFrame()

            df = pd.read_csv("./result.csv")[["name", "home", "draw", "away"]]
            return df


        submit_btn.click(on_submit, inputs=[ligurl, kacincihafta], outputs=tahmintablosu)

        clear_btn.click(clearfunc, outputs=[tahmintablosu, pdf_output_file])

        pdf_download_button.click(
            fn=generate_pdf_from_dataframe,
            inputs=[tahmintablosu],
            outputs=[pdf_output_file]
        )

    blc.launch(share=True)


gradio_interface()