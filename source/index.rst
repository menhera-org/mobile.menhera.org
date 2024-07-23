.. Menhera Mobile (Closed Beta) documentation master file, created by
   sphinx-quickstart on Tue Jul 23 09:21:00 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Menhera Mobile SIM
==========================================

.. NOTE::
   これは現在組織内でテストしているプロジェクトで，他人の通信の用に供しているものではありません。

**Menhera Mobile SIM** は，Menhera.org の通信網を利用したモバイルデータ通信専用SIMです。

SMS を送信する場合は， Menhera.org の SMS ゲートウェイの使用を検討ください。

音声通話は，別途 VoIP を設定することで， **MTNZ** (Menhera.org Telephone Numbering Zone - Menhera.org 電話番号計画区域) の電話網が利用可能です。このSIMを利用することで，インターネットを経由しない通話が可能です。

使用方法
-----------

1. `さくらのセキュアモバイルコネクトのSIM <https://www.amazon.co.jp/dp/B07C2T2NN3>`_ を購入します。
2. 担当者にSIMの登録を依頼します。(**TODO:** 自分で登録できるシステムを準備する)
3. どこからでも AS63806 のネットワーク経由でアクセスできます。(権限がある場合は，該当するイントラネット等にも直接アクセスできます。)

仕様
----

内容
        MVNO卸サービスを利用した仮想モバイル通信網
サービスエリア
        日本国内の NTT Docomo、Softbank、KDDI (au) の LTE サービスエリア
デフォルトキャリア
        Softbank (安定して通信するためには，明示的にローミング先を Softbank に設定することをお勧めします)

        ※管理画面から NTT Docomo、Softbank、KDDI (au) から接続を許可するキャリアを選択可能
対応プロトコル
        IPv4 ユニキャスト通信

        ※IPv6 には現在対応していません。IPv6-only のサイトにはプロキシなどを利用することでアクセスすることができます。

        ※OB25 を実施しています。外部のサーバのポート 25 番にこの SIM からアクセスすることはできません。

        ※MTU=1500のパケットは透過しません。これは，通常，自動設定を利用している場合は問題になりません。

.. toctree::
   :maxdepth: 2
   :caption: ナビゲーション:
   :glob:
   :hidden:

   self
   *

