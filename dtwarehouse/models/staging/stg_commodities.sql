-- import

with source as (
    SELECT
        "Date",
        "Close",
        "simbolo"
    FROM {{ source ('dbsales', 'commodities') }}
),

-- rename columns
renamed as (
    SELECT
        cast("Date" as date) as data,
        "Close" as valor_fechamento,
         simbolo
    FROM source
)

select * from renamed



